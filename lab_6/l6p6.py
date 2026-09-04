import xml.etree.ElementTree as ET

try:
    tree = ET.parse("students.xml")
    root = tree.getroot()
    students = []

    for student in root.findall("student"):
        reg = student.get("id")
        name = student.find("name").text
        dept = student.find("department").text
        marks = int(student.find("marks").text)
        students.append((reg, name, dept, marks))
        print(reg, name, dept, marks)

    search = input("Enter register number to search: ")
    for student in students:
        if student[0] == search:
            print("Found:", student)

    print("Marks above 75:")
    for student in students:
        if student[3] > 75:
            print(student)

    print("Average Marks:", sum(s[3] for s in students) / len(students))
    print("Highest Mark:", max(students, key=lambda x: x[3]))
except FileNotFoundError:
    print("students.xml not found")
except ET.ParseError:
    print("Invalid XML file")
except ValueError:
    print("Invalid marks")
