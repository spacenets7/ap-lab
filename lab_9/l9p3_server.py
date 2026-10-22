import socket

HOST = "127.0.0.1"
PORT = 5003

products = {
    "rice": ("Rice", 60, 25),
    "sugar": ("Sugar", 45, 40),
    "wheat flour": ("Wheat Flour", 38, 15),
    "salt": ("Salt", 20, 0),
}

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((HOST, PORT))
print("Shop server listening on UDP port", PORT)

while True:
    try:
        data, addr = server.recvfrom(1024)
        try:
            text = data.decode("utf-8").strip()
        except UnicodeDecodeError:
            reply = "ERROR Malformed request"
        else:
            if not text:
                reply = "ERROR Product name cannot be empty"
            elif not text.isprintable():
                reply = "ERROR Malformed request"
            elif text.lower() not in products:
                reply = "ERROR Product not found"
            else:
                name, price, qty = products[text.lower()]
                reply = f"{name} | Price: ₹{price} | Available quantity: {qty}"
        server.sendto(reply.encode("utf-8"), addr)
    except OSError:
        continue
