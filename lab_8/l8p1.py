from multiprocessing import Process, Pipe

def analyze(conn):
    temperatures = conn.recv()
    result = (min(temperatures), max(temperatures), sum(temperatures) / len(temperatures))
    conn.send(result)
    conn.close()

if __name__ == "__main__":
    temperatures = [28, 30, 32, 29, 31]
    parent_conn, child_conn = Pipe()

    process = Process(target=analyze, args=(child_conn,))
    process.start()

    parent_conn.send(temperatures)
    minimum, maximum, average = parent_conn.recv()

    process.join()

    print("Temperatures:", temperatures)
    print("Minimum:", minimum)
    print("Maximum:", maximum)
    print(f"Average: {average:.2f}")
