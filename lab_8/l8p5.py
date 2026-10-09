from multiprocessing import Process, Queue

def billing_worker(order_queue, result_queue):
    while True:
        customer = order_queue.get()

        if customer is None:
            break

        customer_id, prices = customer
        bill = sum(prices)
        result_queue.put((customer_id, bill))

if __name__ == "__main__":
    customers = [
        (101, [50, 30, 20]),
        (102, [100, 75]),
        (103, [40, 25, 35]),
        (104, [200, 50]),
        (105, [60, 40, 30])
    ]

    order_queue = Queue()
    result_queue = Queue()

    for customer in customers:
        order_queue.put(customer)

    workers = [Process(target=billing_worker, args=(order_queue, result_queue)) for _ in range(3)]

    for _ in workers:
        order_queue.put(None)

    for worker in workers:
        worker.start()

    bills = [result_queue.get() for _ in customers]

    for worker in workers:
        worker.join()

    revenue = 0
    for customer_id, bill in sorted(bills):
        print(f"Customer {customer_id}: ₹{bill}")
        revenue += bill

    print("Total revenue: ₹", revenue)
