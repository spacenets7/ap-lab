import socket

HOST = "127.0.0.1"
PORT = 5005

tickets = {}


def process(line):
    parts = line.split(maxsplit=1)
    if not parts:
        return "ERROR Invalid request"
    cmd = parts[0].upper()
    arg = parts[1].strip() if len(parts) > 1 else ""
    if cmd == "SUBMIT":
        if not arg:
            return "ERROR Request cannot be empty"
        rid = len(tickets) + 1
        tickets[rid] = {"text": arg, "status": "Open"}
        return f"Request submitted. Request ID: {rid}"
    if cmd == "VIEW":
        try:
            rid = int(arg)
        except ValueError:
            return "ERROR Invalid request ID"
        if rid not in tickets:
            return "ERROR Request ID not found"
        t = tickets[rid]
        return f"Request ID: {rid} | Request: {t['text']} | Status: {t['status']}"
    return "ERROR Invalid request"


def serve(conn):
    f = conn.makefile("rw", encoding="utf-8", errors="replace", newline="\n")
    for line in f:
        line = line.strip()
        if line.upper() == "EXIT":
            f.write("Goodbye\n")
            f.flush()
            break
        f.write(process(line) + "\n")
        f.flush()


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen(1)
print("Help desk server listening on port", PORT)

while True:
    conn, addr = server.accept()
    print("Connected:", addr)
    conn.settimeout(60)
    try:
        serve(conn)
    except socket.timeout:
        print("Client timed out")
    except OSError:
        print("Client disconnected unexpectedly")
    finally:
        conn.close()
