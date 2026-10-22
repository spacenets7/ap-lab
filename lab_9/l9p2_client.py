import socket

HOST = "127.0.0.1"
PORT = 5002

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


def read_marks():
    return [input(f"Marks {i}: ").strip() for i in (1, 2, 3)]


try:
    while True:
        print("\n1. Add record\n2. Search by roll number\n3. Update marks\n4. Show result\n5. Exit")
        choice = input("Choice: ").strip()
        if choice == "5":
            print(send("EXIT"))
            break
        if choice == "1":
            roll = input("Roll number: ").strip()
            name = input("Name: ").strip()
            dept = input("Department: ").strip()
            print(send("|".join(["ADD", roll, name, dept] + read_marks())))
        elif choice == "2":
            roll = input("Roll number: ").strip()
            print(send(f"SEARCH|{roll}"))
        elif choice == "3":
            roll = input("Roll number: ").strip()
            print(send("|".join(["UPDATE", roll] + read_marks())))
        elif choice == "4":
            roll = input("Roll number: ").strip()
            print(send(f"RESULT|{roll}"))
        else:
            print("Invalid choice")
except socket.timeout:
    print("Server timed out.")
except OSError:
    print("Connection lost.")
finally:
    s.close()
