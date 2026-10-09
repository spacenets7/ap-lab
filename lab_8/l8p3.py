from threading import Thread, Lock

stock = {"Rice": 10, "Milk": 5, "Bread": 8}
transactions = []
stock_lock = Lock()

def supply(supplier, items):
    with stock_lock:
        for product, quantity in items.items():
            stock[product] = stock.get(product, 0) + quantity
            transactions.append(f"{supplier} supplied {quantity} {product}")
            print(f"{supplier} added {quantity} {product}")

def purchase(customer, product, quantity):
    with stock_lock:
        if stock.get(product, 0) >= quantity:
            stock[product] -= quantity
            transactions.append(f"{customer} bought {quantity} {product}: SUCCESS")
            print(f"{customer}: bought {quantity} {product}")
        else:
            transactions.append(f"{customer} bought {quantity} {product}: REJECTED")
            print(f"{customer}: purchase of {quantity} {product} rejected")

if __name__ == "__main__":
    threads = [
        Thread(target=supply, args=("Supplier 1", {"Rice": 5, "Bread": 4})),
        Thread(target=supply, args=("Supplier 2", {"Milk": 10})),
        Thread(target=purchase, args=("Customer 1", "Rice", 8)),
        Thread(target=purchase, args=("Customer 2", "Milk", 12)),
        Thread(target=purchase, args=("Customer 3", "Bread", 20)),
        Thread(target=purchase, args=("Customer 4", "Rice", 10)),
        Thread(target=purchase, args=("Customer 5", "Milk", 4))
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    successful = sum("SUCCESS" in item for item in transactions)
    rejected = sum("REJECTED" in item for item in transactions)

    print("\nTransaction record:")
    for item in transactions:
        print(item)

    print("\nFinal stock:", stock)
    print("Successful purchases:", successful)
    print("Rejected purchases:", rejected)
