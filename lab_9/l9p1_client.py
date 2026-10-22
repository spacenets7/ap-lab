import socket

HOST = "127.0.0.1"
PORT = 5001

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
        print("\n1. Check balance\n2. Deposit\n3. Withdraw\n4. Exit")
        choice = input("Choice: ").strip()
        if choice == "4":
            print(send("EXIT"))
            break
        if choice not in ("1", "2", "3"):
            print("Invalid choice")
            continue
        acc = input("Account number: ").strip()
        if choice == "1":
            request = f"BALANCE {acc}"
        else:
            amount = input("Amount: ").strip()
            action = "DEPOSIT" if choice == "2" else "WITHDRAW"
            request = f"{action} {acc} {amount}"
        print(send(request))
except socket.timeout:
    print("Server timed out.")
except OSError:
    print("Connection lost.")
finally:
    s.close()
