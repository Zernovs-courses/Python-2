import socketserver
import threading


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    daemon_threads = True
    allow_reuse_address = True


class DateHandler(socketserver.StreamRequestHandler):
    def handle(self):
        client = f"{self.client_address} on {threading.current_thread().name}"
        print(f"Connected: {client}")

        while True:
            data = self.rfile.readline()
            if not data:
                break
            self.wfile.write(data.decode().upper().encode())

        print(f"Closed: {client}")


with ThreadedTCPServer(("", 59090), DateHandler) as server:
    print("Server is running...")
    server.serve_forever()
