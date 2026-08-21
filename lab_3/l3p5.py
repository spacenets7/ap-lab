consumers = {}

n = int(input("Enter number of consumers: "))
for _ in range(n):
    number = input("Consumer number: ")
    units = float(input("Units consumed: "))
    consumers[number] = units

while True:
    print("\n1. Display Records\n2. Search Consumer\n3. Above 300 Units\n4. Highest Consumption\n5. Average Consumption\n6. Update Consumption\n7. Total Consumers\n8. Exit")
    ch = input("Enter choice: ")

    if ch == "1":
        print(consumers)

    elif ch == "2":
        number = input("Consumer number: ")
        print(consumers.get(number, "Consumer not found"))

    elif ch == "3":
        for number, units in consumers.items():
            if units > 300:
                print(number, units)

    elif ch == "4":
        if consumers:
            number = max(consumers, key=consumers.get)
            print(number, consumers[number])

    elif ch == "5":
        if consumers:
            print("Average:", sum(consumers.values()) / len(consumers))

    elif ch == "6":
        number = input("Consumer number: ")
        if number in consumers:
            consumers[number] = float(input("New units: "))
        else:
            print("Consumer not found")

    elif ch == "7":
        print("Total consumers:", len(consumers))

    elif ch == "8":
        break

    else:
        print("Invalid choice")
