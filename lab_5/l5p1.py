numbers = list(map(int, input("Enter numbers separated by space: ").split()))

try:
    index = int(input("Enter index: "))
    print("Element:", numbers[index])
except ValueError:
    print("Index must be an integer")
except IndexError:
    print("Index out of range")
