class InvalidExamDataError(Exception):
    pass

try:
    student_id = int(input("Enter Student ID: "))
    attempted = int(input("Enter questions attempted: "))
    correct = int(input("Enter correct answers: "))
    wrong = int(input("Enter wrong answers: "))

    if attempted < 0 or attempted > 100:
        raise InvalidExamDataError("Attempted questions must be between 0 and 100")
    if correct < 0 or wrong < 0:
        raise InvalidExamDataError("Correct and wrong answers cannot be negative")
    if correct + wrong != attempted:
        raise InvalidExamDataError("Correct and wrong answers must equal attempted questions")

    score = correct * 4 - wrong
    status = "Pass" if score >= 160 else "Fail"

    print("Correct Answers:", correct)
    print("Wrong Answers:", wrong)
    print("Final Score:", score)
    print("Result Status:", status)

except ValueError:
    print("All values must be integers")
except InvalidExamDataError as e:
    print(e)
