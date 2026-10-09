from multiprocessing import Pool

def analyze_department(data):
    department, students = data
    results = []

    for roll, marks in students:
        total = sum(marks)
        average = total / len(marks)
        passed = all(mark >= 40 for mark in marks)
        results.append((roll, marks, total, average, passed))

    topper = max(results, key=lambda student: student[2])
    passed_count = sum(student[4] for student in results)

    return department, results, topper, passed_count

if __name__ == "__main__":
    departments = {
        "CSE": [(101, [85, 90, 78]), (102, [70, 65, 80]), (103, [35, 60, 55])],
        "MnC": [(201, [92, 88, 95]), (202, [75, 81, 79]), (203, [45, 38, 60])],
        "ECE": [(301, [68, 72, 74]), (302, [88, 91, 84]), (303, [55, 62, 58])]
    }

    with Pool() as pool:
        reports = pool.map(analyze_department, departments.items())

    for department, students, topper, passed_count in reports:
        print(f"\nDepartment: {department}")

        for roll, marks, total, average, passed in students:
            status = "Pass" if passed else "Fail"
            print(f"Roll: {roll}, Total: {total}, Average: {average:.2f}, {status}")

        print(f"Topper: {topper[0]} with {topper[2]} marks")
        print("Students passed all subjects:", passed_count)
