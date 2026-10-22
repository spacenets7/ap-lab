import os
import socket

HOST = "127.0.0.1"
PORT = 5004
FOLDER = "server_files"

os.makedirs(FOLDER, exist_ok=True)
sample = os.path.join(FOLDER, "notes.txt")
if not os.path.exists(sample):
    with open(sample, "wb") as out:
        out.write(b"Hello\n")


def valid_name(name):
    if name in ("", ".", ".."):
        return False
    if os.path.basename(name) != name or "\\" in name:
        return False
    return True


def serve(conn):
    f = conn.makefile("rb")
    while True:
        line = f.readline()
        if not line:
            break
        parts = line.decode("utf-8", errors="replace").strip().split(maxsplit=1)
        if not parts:
            conn.sendall(b"ERROR Invalid request\n")
            continue
        cmd = parts[0].upper()
        if cmd == "EXIT":
            break
        if cmd != "GET" or len(parts) != 2:
            conn.sendall(b"ERROR Invalid request\n")
            continue
        name = parts[1]
        if not valid_name(name):
            conn.sendall(b"ERROR Invalid filename\n")
            continue
        path = os.path.join(FOLDER, name)
        if not os.path.isfile(path):
            conn.sendall(b"ERROR File not found\n")
            continue
        try:
            with open(path, "rb") as fh:
                data = fh.read()
        except OSError:
            conn.sendall(b"ERROR Could not read file\n")
            continue
        conn.sendall(f"OK {len(data)}\n".encode() + data)


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen(1)
print("File server listening on port", PORT)

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
