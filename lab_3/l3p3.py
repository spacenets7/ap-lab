students = {}
branches = set()

while True:
    print("\n1. Add Student\n2. Search Student\n3. Display All Students\n4. Display Topper\n5. Display Branches\n6. Display Passed Students\n7. Remove Failed Student\n8. Exit")
    ch = input("Enter choice: ")

    if ch == "1":
        usn = input("USN: ")
        if usn in students:
            print("Duplicate USN")
            continue
        name = input("Name: ")
        branch = input("Branch: ")
        marks = tuple(map(int, input("Enter 3 marks: ").split()))
        if len(marks) != 3:
            print("Enter exactly 3 marks")
            continue
        students[usn] = (name, branch, marks)
        branches.add(branch)

    elif ch == "2":
        usn = input("USN: ")
        if usn in students:
            name, branch, marks = students[usn]
            print(usn, name, branch, marks, sum(marks), sum(marks) / 3)
        else:
            print("Student not found")

    elif ch == "3":
        for usn, (name, branch, marks) in students.items():
            print(usn, name, branch, marks, sum(marks), sum(marks) / 3)

    elif ch == "4":
        if students:
            usn, record = max(students.items(), key=lambda x: sum(x[1][2]))
            print(usn, record, sum(record[2]))

    elif ch == "5":
        print(branches)

    elif ch == "6":
        for usn, (name, branch, marks) in students.items():
            if all(m >= 35 for m in marks):
                print(usn, name, branch, marks)

    elif ch == "7":
        for usn, (name, branch, marks) in list(students.items()):
            if sum(m < 35 for m in marks) > 2:
                del students[usn]
                print("Removed:", usn)

    elif ch == "8":
        break

    else:
        print("Invalid choice")
