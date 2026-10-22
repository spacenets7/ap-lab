import socket

HOST = "127.0.0.1"
PORT = 5006

notices = {}


def process(line, state):
    parts = line.split(maxsplit=1)
    if not parts:
        return ["ERROR Invalid request"]
    cmd = parts[0].upper()
    arg = parts[1].strip() if len(parts) > 1 else ""
    if cmd == "ROLE":
        if arg.lower() in ("staff", "student"):
            state["role"] = arg.lower()
            return [f"Role set to {state['role']}"]
        return ["ERROR Invalid role. Use staff or student"]
    if state["role"] is None:
        return ["ERROR Set a role first"]
    if cmd == "ADD":
        if state["role"] != "staff":
            return ["ERROR Only staff can add notices"]
        if not arg:
            return ["ERROR Notice cannot be empty"]
        nid = len(notices) + 1
        notices[nid] = arg
        return [f"Notice added with ID {nid}"]
    if cmd == "LIST":
        if not notices:
            return ["No notices available"]
        return [f"Notice {i}: {t}" for i, t in notices.items()]
    if cmd == "GET":
        try:
            nid = int(arg)
        except ValueError:
            return ["ERROR Invalid notice ID"]
        if nid not in notices:
            return ["ERROR Notice not found"]
        return [f"Notice {nid}: {notices[nid]}"]
    return ["ERROR Invalid request"]


def serve(conn):
    f = conn.makefile("rw", encoding="utf-8", errors="replace", newline="\n")
    state = {"role": None}
    for line in f:
        line = line.strip()
        if line.upper() == "EXIT":
            break
        reply = process(line, state)
        f.write("\n".join(reply) + "\nEND\n")
        f.flush()


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen(1)
print("Notice board server listening on port", PORT)

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
