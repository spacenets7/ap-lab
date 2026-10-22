import socket

HOST = "127.0.0.1"
PORT = 5005

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
    reply = f.readline()
    if not reply:
        raise ConnectionError
    return reply.strip()


try:
    while True:
        print("\n1. Submit request\n2. View request\n3. Exit")
        choice = input("Choice: ").strip()
        if choice == "3":
            print(send("EXIT"))
            break
        if choice == "1":
            text = input("Request: ").strip()
            if not text:
                print("Request cannot be empty")
                continue
            print(send(f"SUBMIT {text}"))
        elif choice == "2":
            rid = input("Request ID: ").strip()
            print(send(f"VIEW {rid}"))
        else:
            print("Invalid choice")
except socket.timeout:
    print("Server timed out.")
except OSError:
    print("Connection lost.")
finally:
    s.close()
