class InvalidMarkError(Exception):
    pass

filename = input("Enter Filename: ")

try:
    total = 0
    count = 0
    with open(filename) as fp:
        for line_no, line in enumerate(fp, 1):
            try:
                mark = int(line.strip())
            except ValueError:
                print("Non-numeric value at line", line_no)
                continue
            if mark < 0 or mark > 100:
                raise InvalidMarkError(f"Invalid mark at line {line_no}")
            total += mark
            count += 1

    if count == 0:
        print("File is empty")
    else:
        print("Total:", total)
        print("Average:", total / count)
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission denied")
except InvalidMarkError as e:
    print(e)
