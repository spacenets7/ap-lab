import socket

HOST = "127.0.0.1"
PORT = 5001

accounts = {
    "1001": {"name": "Anu", "balance": 5000},
    "1002": {"name": "Ravi", "balance": 12000},
    "1003": {"name": "Meena", "balance": 800},
}


def fmt(x):
    if x == int(x):
        return f"{int(x):,}"
    return f"{x:,.2f}"


def parse_amount(text):
    try:
        amount = float(text)
    except ValueError:
        return None
    if not amount > 0 or amount == float("inf"):
        return None
    return amount


def process(line):
    parts = line.split()
    if not parts:
        return "ERROR Empty request"
    cmd = parts[0].upper()
    if cmd not in ("BALANCE", "DEPOSIT", "WITHDRAW"):
        return "ERROR Invalid request"
    if len(parts) < 2:
        return "ERROR Account number missing"
    acc = parts[1]
    if acc not in accounts:
        return "ERROR Account not found"
    account = accounts[acc]
    if cmd == "BALANCE":
        return f"Balance for {account['name']}: ₹{fmt(account['balance'])}"
    if len(parts) != 3:
        return "ERROR Amount missing or invalid request"
    amount = parse_amount(parts[2])
    if amount is None:
        return "ERROR Invalid amount. Amount must be a positive number"
    if cmd == "DEPOSIT":
        account["balance"] += amount
        return f"Deposit successful. Updated balance: ₹{fmt(account['balance'])}"
    if amount > account["balance"]:
        return f"ERROR Insufficient funds. Balance: ₹{fmt(account['balance'])}"
    account["balance"] -= amount
    return f"Withdrawal successful. Updated balance: ₹{fmt(account['balance'])}"


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
print("Bank server listening on port", PORT)

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
