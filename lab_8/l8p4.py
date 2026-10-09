from threading import Thread, Lock

available_seats = list(range(1, 21))
seat_lock = Lock()

def book(customer, count):
    with seat_lock:
        if len(available_seats) >= count:
            seats = available_seats[:count]
            del available_seats[:count]
            print(f"{customer}: booking successful, seats {seats}")
        else:
            print(f"{customer}: booking rejected, not enough seats")

if __name__ == "__main__":
    requests = [
        ("Customer 1", 3),
        ("Customer 2", 5),
        ("Customer 3", 4),
        ("Customer 4", 6),
        ("Customer 5", 4)
    ]

    threads = [Thread(target=book, args=request) for request in requests]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print("Available seats:", len(available_seats))
    print("Remaining seat numbers:", available_seats)
