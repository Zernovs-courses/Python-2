import socketserver
import threading

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    daemon_threads = True
    allow_reuse_address = True

class CapHandler(socketserver.StreamRequestHandler):
    def handle(self) -> None:
        client = f"{self.client_address} on {threading.current_thread().getName()}"
        print(f"Connected: {client}")

        while True:
            data = self.rfile.readline()
            if not data:
                break
            self.wfile.write(data.decode().upper().encode())

        print(f"Closed: {client}")

with ThreadedTCPServer(('', 59898), CapHandler) as server:
    print("Server is running...")
    server.serve_forever()