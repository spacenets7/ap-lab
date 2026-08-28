class InvalidPINError(Exception):
    pass

class InsufficientBalanceError(Exception):
    pass

class InvalidAmountError(Exception):
    pass

pin = "1234"
balance = 30000

try:
    for attempt in range(3):
        entered_pin = input("Enter PIN: ")
        if entered_pin == pin:
            break
        print("Invalid PIN")
    else:
        raise InvalidPINError("Maximum PIN attempts exceeded")

    amount = int(input("Enter withdrawal amount: "))

    if amount <= 0 or amount % 100 != 0:
        raise InvalidAmountError("Amount must be positive and a multiple of 100")
    if amount > 20000:
        raise InvalidAmountError("Maximum withdrawal is 20000")
    if amount > balance:
        raise InsufficientBalanceError("Insufficient balance")

    balance -= amount
    print("Withdrawal successful")
    print("Updated balance:", balance)

except (InvalidPINError, InvalidAmountError, InsufficientBalanceError) as e:
    print(e)
except ValueError:
    print("Enter a valid amount")
