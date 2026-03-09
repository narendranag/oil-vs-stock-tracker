#!/usr/bin/env python3
"""Simple local server: serves static files and proxies Yahoo Finance API."""

import http.server
import json
import os
import urllib.request
import urllib.parse
import urllib.error
from pathlib import Path

PORT = int(os.environ.get("PORT", 3456))
STATIC_DIR = Path(__file__).parent

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(STATIC_DIR), **kwargs)

    def do_GET(self):
        if self.path.startswith("/api/chart/"):
            self.handle_chart_api()
        else:
            super().do_GET()

    def handle_chart_api(self):
        # /api/chart/AAPL?range=6mo&interval=1wk
        parts = self.path.split("?", 1)
        symbol = urllib.parse.unquote(parts[0].replace("/api/chart/", ""))
        query = parts[1] if len(parts) > 1 else ""

        yahoo_url = f"https://query1.finance.yahoo.com/v8/finance/chart/{urllib.parse.quote(symbol, safe='=')}?{query}"

        try:
            req = urllib.request.Request(yahoo_url, headers={
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
            })
            with urllib.request.urlopen(req, timeout=10) as resp:
                data = resp.read()
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
                self.wfile.write(data)
        except urllib.error.HTTPError as e:
            body = e.read()
            self.send_response(e.code)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(body)
        except Exception as e:
            self.send_response(502)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"error": str(e)}).encode())

    def log_message(self, format, *args):
        # Quieter logging
        if "/api/" in str(args[0]):
            super().log_message(format, *args)

if __name__ == "__main__":
    server = http.server.HTTPServer(("0.0.0.0", PORT), Handler)
    print(f"Dashboard running at http://localhost:{PORT}")
    server.serve_forever()
