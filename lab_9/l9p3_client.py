import socket

SERVER = ("127.0.0.1", 5003)
RETRIES = 3

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.settimeout(2)

while True:
    name = input("\nProduct name (or EXIT): ").strip()
    if name.upper() == "EXIT":
        break
    if not name:
        print("Product name cannot be empty")
        continue
    reply = None
    for attempt in range(1, RETRIES + 1):
        try:
            s.sendto(name.encode("utf-8"), SERVER)
            data, _ = s.recvfrom(1024)
            reply = data.decode("utf-8", errors="replace")
            break
        except socket.timeout:
            print(f"No response (attempt {attempt}/{RETRIES})")
        except OSError:
            print("Server unreachable")
            break
    if reply is None:
        print("Enquiry failed. Try again.")
    else:
        print(reply)

s.close()
