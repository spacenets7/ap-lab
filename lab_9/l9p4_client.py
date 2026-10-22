import os
import socket

HOST = "127.0.0.1"
PORT = 5004

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

rf = s.makefile("rb")

try:
    while True:
        name = input("\nFilename (or EXIT): ").strip()
        if name.upper() == "EXIT":
            s.sendall(b"EXIT\n")
            break
        if name in ("", ".", "..") or os.path.basename(name) != name or "\\" in name:
            print("Invalid filename")
            continue
        s.sendall(f"GET {name}\n".encode())
        header = rf.readline().decode("utf-8", errors="replace").strip()
        if not header:
            print("Server disconnected.")
            break
        if header.startswith("ERROR"):
            print(header)
            continue
        parts = header.split()
        if len(parts) != 2 or parts[0] != "OK" or not parts[1].isdigit():
            print("Invalid response from server")
            break
        size = int(parts[1])
        data = rf.read(size)
        with open(name, "wb") as out:
            out.write(data)
        if len(data) == size:
            print(f"File saved as {name}. Expected: {size} bytes. Received: {len(data)} bytes. Transfer complete.")
        else:
            os.remove(name)
            print(f"Transfer incomplete. Expected: {size} bytes. Received: {len(data)} bytes. File discarded.")
            break
except socket.timeout:
    print("Server timed out.")
except OSError:
    print("Connection lost.")
finally:
    s.close()
