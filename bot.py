import os
import time
import requests
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading

WEBHOOK_URL = os.getenv("WEBHOOK_URL")

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"BOT RUNNING")

def run_server():
    server = HTTPServer(("0.0.0.0", 10000), Handler)
    server.serve_forever()

threading.Thread(target=run_server, daemon=True).start()

def notify(message):
    requests.post(WEBHOOK_URL, json={"content": message}, timeout=10)

print("JFC BOT START")
print("通知送信前")
notify("✅ JFC通知BOT 起動中")
print("通知送信後")

while True:
    print("BOT RUNNING")
    time.sleep(60)
    

