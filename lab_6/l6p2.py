filename = "employees.txt"

while True:
    print("\n1. Create")
    print("2. Add")
    print("3. Display")
    print("4. Search")
    print("5. Salary above 50000")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        open(filename, "w").close()
        print("File created")
    elif choice == "2":
        emp_id = input("Enter employee ID: ")
        name = input("Enter employee name: ")
        salary = input("Enter salary: ")
        with open(filename, "a") as f:
            f.write(f"{emp_id}|{name}|{salary}\n")
    elif choice == "3":
        try:
            with open(filename) as f:
                print(f.read(), end="")
        except FileNotFoundError:
            print("File not found")
    elif choice == "4":
        emp_id = input("Enter employee ID to search: ")
        found = False
        try:
            with open(filename) as f:
                for line in f:
                    data = line.strip().split("|")
                    if data[0] == emp_id:
                        print(line.strip())
                        found = True
                        break
            if not found:
                print("Employee not found")
        except FileNotFoundError:
            print("File not found")
    elif choice == "5":
        try:
            with open(filename) as f:
                for line in f:
                    data = line.strip().split("|")
                    if float(data[2]) > 50000:
                        print(line.strip())
        except FileNotFoundError:
            print("File not found")
    elif choice == "6":
        break
    else:
        print("Invalid choice")
