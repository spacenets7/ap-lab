from threading import Thread, Lock
from queue import Queue

orders = [
    (101, "Pizza", 2, 250),
    (102, "Burger", 3, 120),
    (103, "Pasta", 1, 180),
    (104, "Sandwich", 2, 100),
    (105, "Noodles", 2, 150)
]

order_queue = Queue()
sales_lock = Lock()
total_sales = [0]

def chef(name):
    while True:
        order = order_queue.get()

        if order is None:
            order_queue.task_done()
            break

        order_id, dish, quantity, price = order
        amount = quantity * price

        with sales_lock:
            total_sales[0] += amount

        print(f"{name} processed Order {order_id}: {dish}, Total = ₹{amount}")
        order_queue.task_done()

if __name__ == "__main__":
    for order in orders:
        order_queue.put(order)

    chefs = [Thread(target=chef, args=(f"Chef {i}",)) for i in range(1, 4)]

    for thread in chefs:
        thread.start()

    for _ in chefs:
        order_queue.put(None)

    order_queue.join()

    for thread in chefs:
        thread.join()

    print(f"Total sales: ₹{total_sales[0]}")
