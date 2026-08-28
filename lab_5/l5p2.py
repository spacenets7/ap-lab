try:
    marks = []
    for i in range(5):
        mark = float(input(f"Enter marks for subject {i + 1}: "))
        if mark < 0 or mark > 100:
            raise ValueError("Marks must be between 0 and 100")
        marks.append(mark)

    total = sum(marks)
    average = total / 5

    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    else:
        grade = "F"

    print("Total:", total)
    print("Average:", average)
    print("Grade:", grade)

except ValueError as e:
    print("Invalid input:", e)

finally:
    print("Result processing completed")
