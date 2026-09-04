students = []

for i in range(5):
    reg = input("Enter register number: ")
    name = input("Enter name: ")
    marks = input("Enter marks: ")
    students.append(f"{reg}|{name}|{marks}")

with open("students.txt", "w") as f:
    for student in students:
        f.write(student + "\n")

with open("students.txt", "r") as f:
    records = f.readlines()

for record in records:
    print(record.strip())

print("Number of records:", len(records))
