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

print("JFC BOT START")

sent = False

while True:
    try:
        if not sent:
            print("SEND START")

            requests.post(
                WEBHOOK_URL,
                json={"content": "✅ JFC BOT 起動成功"}
            )
            print("Discord通知送信")
            sent = True

        print("BOT RUNNING")
        time.sleep(30)

    except Exception as e:
        print("ERROR:", e)
        import traceback
        traceback.print_exc()
        time.sleep(30)
