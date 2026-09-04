import struct

class InvalidRecordError(Exception):
    pass

filename = "employees.dat"
record_format = "<i20sd"
record_size = struct.calcsize(record_format)

try:
    with open(filename, "wb") as f:
        for i in range(5):
            emp_id = int(input("Enter employee ID: "))
            name = input("Enter employee name: ").encode()[:20].ljust(20, b" ")
            salary = float(input("Enter salary: "))
            f.write(struct.pack(record_format, emp_id, name, salary))

    record_no = int(input("Enter record number: "))
    if record_no < 1 or record_no > 5:
        raise InvalidRecordError("Invalid record number")

    with open(filename, "rb") as f:
        f.seek((record_no - 1) * record_size)
        data = f.read(record_size)
        emp_id, name, salary = struct.unpack(record_format, data)
        print(emp_id, name.decode().strip(), salary)

    update_id = int(input("Enter employee ID to update: "))
    new_salary = float(input("Enter new salary: "))

    with open(filename, "r+b") as f:
        for i in range(5):
            f.seek(i * record_size)
            data = f.read(record_size)
            emp_id, name, salary = struct.unpack(record_format, data)
            if emp_id == update_id:
                f.seek(i * record_size)
                f.write(struct.pack(record_format, emp_id, name, new_salary))
                break

    with open(filename, "rb") as f:
        for i in range(5):
            data = f.read(record_size)
            emp_id, name, salary = struct.unpack(record_format, data)
            print(emp_id, name.decode().strip(), salary)
except ValueError:
    print("Invalid numeric input")
except InvalidRecordError as e:
    print(e)
except FileNotFoundError:
    print("File not found")
except struct.error:
    print("Corrupted or incomplete record")
