import socket

HOST = "127.0.0.1"
PORT = 5006

try:
    s = socket.create_connection((HOST, PORT), timeout=10)
except ConnectionRefusedError:
    print("Connection refused. Start the server first.")
    raise SystemExit
except socket.timeout:
    print("Connection timed out.")
    raise SystemExit
except OSError as e:
    print("Could not connect:", e)
    raise SystemExit

f = s.makefile("rw", encoding="utf-8", errors="replace", newline="\n")


def send(msg):
    f.write(msg + "\n")
    f.flush()
    lines = []
    while True:
        line = f.readline()
        if not line:
            raise ConnectionError
        line = line.rstrip("\n")
        if line == "END":
            return lines
        lines.append(line)


try:
    while True:
        role = input("Role (staff/student): ").strip()
        reply = send(f"ROLE {role}")
        print("\n".join(reply))
        if not reply[0].startswith("ERROR"):
            break
    while True:
        print("\n1. Add notice\n2. List notices\n3. Get notice by ID\n4. Exit")
        choice = input("Choice: ").strip()
        if choice == "4":
            f.write("EXIT\n")
            f.flush()
            break
        if choice == "1":
            text = input("Notice: ").strip()
            if not text:
                print("Notice cannot be empty")
                continue
            print("\n".join(send(f"ADD {text}")))
        elif choice == "2":
            print("\n".join(send("LIST")))
        elif choice == "3":
            nid = input("Notice ID: ").strip()
            print("\n".join(send(f"GET {nid}")))
        else:
            print("Invalid choice")
except socket.timeout:
    print("Server timed out.")
except OSError:
    print("Connection lost.")
finally:
    s.close()
