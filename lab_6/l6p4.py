import struct

filename = "employees.dat"
record_format = "i20sf"
record_size = struct.calcsize(record_format)

n = int(input("Enter number of employees: "))

with open(filename, "wb") as f:
    for i in range(n):
        emp_id = int(input("Enter employee ID: "))
        name = input("Enter employee name: ").encode()[:20].ljust(20, b" ")
        salary = float(input("Enter salary: "))
        f.write(struct.pack(record_format, emp_id, name, salary))

with open(filename, "rb") as f:
    while True:
        data = f.read(record_size)
        if not data:
            break
        emp_id, name, salary = struct.unpack(record_format, data)
        print(emp_id, name.decode().strip(), salary)

search_id = int(input("Enter employee ID to search: "))
found = False
with open(filename, "rb") as f:
    while True:
        data = f.read(record_size)
        if not data:
            break
        emp_id, name, salary = struct.unpack(record_format, data)
        if emp_id == search_id:
            print("Name:", name.decode().strip())
            print("Salary:", salary)
            found = True
            break
if not found:
    print("Employee not found")
