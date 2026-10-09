from multiprocessing import Process, Value, Lock, Queue

def transact(action, amount, balance, lock, results):
    with lock:
        if action == "deposit":
            balance.value += amount
            message = f"Deposited ₹{amount}"
            status = "SUCCESS"
        elif balance.value >= amount:
            balance.value -= amount
            message = f"Withdrew ₹{amount}"
            status = "SUCCESS"
        else:
            message = f"Withdrawal of ₹{amount} rejected"
            status = "REJECTED"

        results.put((action, amount, status, message, balance.value))

if __name__ == "__main__":
    balance = Value("i", 10000)
    lock = Lock()
    results = Queue()

    transactions = [
        ("deposit", 2500),
        ("withdraw", 4000),
        ("deposit", 1000),
        ("withdraw", 3000),
        ("withdraw", 15000)
    ]

    processes = [
        Process(target=transact, args=(action, amount, balance, lock, results))
        for action, amount in transactions
    ]

    for process in processes:
        process.start()

    outcomes = [results.get() for _ in processes]

    for process in processes:
        process.join()

    successful = 0
    rejected = 0

    for action, amount, status, message, current_balance in outcomes:
        print(f"{message}: {status}")
        if status == "SUCCESS":
            successful += 1
        else:
            rejected += 1

    print("Final balance: ₹", balance.value)
    print("Successful transactions:", successful)
    print("Rejected transactions:", rejected)
