import socketserver
from datetime import datetime


class DateHandler(socketserver.StreamRequestHandler):
    def handle(self):
        self.wfile.write(f"{datetime.now().isoformat()}\n".encode())


with socketserver.TCPServer(("", 59090), DateHandler) as server:
    print("Server is running...")
    server.serve_forever()
