import socket

HOST = "127.0.0.1"
PORT = 5002

students = {}


def parse_marks(items):
    marks = []
    for item in items:
        try:
            m = float(item)
        except ValueError:
            return None, "ERROR Marks must be numeric"
        if not 0 <= m <= 100:
            return None, "ERROR Marks must be between 0 and 100"
        marks.append(m)
    return marks, None


def marks_text(marks):
    return ", ".join(f"{m:g}" for m in marks)


def process(line):
    parts = [p.strip() for p in line.split("|")]
    cmd = parts[0].upper()
    if cmd == "ADD":
        if len(parts) != 7:
            return "ERROR ADD needs roll, name, department and 3 marks"
        roll, name, dept = parts[1], parts[2], parts[3]
        if not roll or not name or not dept:
            return "ERROR Roll number, name and department cannot be empty"
        if roll in students:
            return "ERROR Duplicate roll number"
        marks, err = parse_marks(parts[4:7])
        if err:
            return err
        students[roll] = {"name": name, "dept": dept, "marks": marks}
        return "Record added"
    if cmd in ("SEARCH", "UPDATE", "RESULT"):
        if len(parts) < 2 or not parts[1]:
            return "ERROR Roll number missing"
        roll = parts[1]
        if roll not in students:
            return "ERROR Record not found"
        student = students[roll]
        if cmd == "SEARCH":
            return (f"Roll: {roll} | Name: {student['name']} | "
                    f"Department: {student['dept']} | Marks: {marks_text(student['marks'])}")
        if cmd == "UPDATE":
            if len(parts) != 5:
                return "ERROR UPDATE needs roll and 3 marks"
            marks, err = parse_marks(parts[2:5])
            if err:
                return err
            student["marks"] = marks
            return "Marks updated"
        marks = student["marks"]
        total = sum(marks)
        average = total / 3
        result = "Pass" if all(m >= 40 for m in marks) else "Fail"
        return f"Total: {total:g} | Average: {average:.2f} | Result: {result}"
    return "ERROR Invalid request"


def serve(conn):
    f = conn.makefile("rw", encoding="utf-8", errors="replace", newline="\n")
    for line in f:
        line = line.strip()
        if line.upper() == "EXIT":
            f.write("Goodbye\n")
            f.flush()
            break
        f.write(process(line) + "\n")
        f.flush()


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen(1)
print("Student server listening on port", PORT)

while True:
    conn, addr = server.accept()
    print("Connected:", addr)
    conn.settimeout(60)
    try:
        serve(conn)
    except socket.timeout:
        print("Client timed out")
    except OSError:
        print("Client disconnected unexpectedly")
    finally:
        conn.close()
