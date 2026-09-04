import xml.etree.ElementTree as ET

root = ET.Element("students")

for i in range(5):
    reg = input("Enter register number: ")
    name = input("Enter student name: ")
    dept = input("Enter department: ")
    marks = input("Enter marks: ")

    student = ET.SubElement(root, "student", id=reg)
    ET.SubElement(student, "name").text = name
    ET.SubElement(student, "department").text = dept
    ET.SubElement(student, "marks").text = marks

tree = ET.ElementTree(root)
ET.indent(tree)
tree.write("students.xml", encoding="utf-8", xml_declaration=True)
print(ET.tostring(root, encoding="unicode"))
