import gzip

filename = "employees.txt.gz"

try:
    with gzip.open(filename, "wt") as f:
        for i in range(5):
            emp_id = int(input("Enter employee ID: "))
            name = input("Enter employee name: ")
            dept = input("Enter department: ")
            salary = float(input("Enter salary: "))
            f.write(f"{emp_id}|{name}|{dept}|{salary}\n")

    total = 0
    with gzip.open(filename, "rt") as f:
        for line in f:
            emp_id, name, dept, salary = line.strip().split("|")
            salary = float(salary)
            print(emp_id, name, dept, salary)
            if salary > 50000:
                print("Salary above 50000:", name)
            total += salary
    print("Total Salary:", total)
except FileNotFoundError:
    print("File not found")
except gzip.BadGzipFile:
    print("Invalid gzip file")
except EOFError:
    print("Incomplete gzip file")
except ValueError:
    print("Invalid employee ID or salary")
except OSError:
    print("File processing error")
