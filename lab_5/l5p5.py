class InvalidPurchaseError(Exception):
    pass

class InsufficientBalanceError(Exception):
    pass

try:
    product_price = float(input("Enter Product Price: "))
    quantity = int(input("Enter Quantity: "))
    balance = float(input("Enter Wallet Balance: "))

    if product_price <= 0:
        raise InvalidPurchaseError("Product price must be greater than zero")
    if quantity < 1 or quantity > 10:
        raise InvalidPurchaseError("Quantity must be between 1 and 10")
    if balance < 0:
        raise InvalidPurchaseError("Wallet balance cannot be negative")

    purchase_amount = product_price * quantity
    discount = purchase_amount * 0.10
    final_amount = purchase_amount - discount

    if final_amount > balance:
        raise InsufficientBalanceError("Insufficient wallet balance")

    balance -= final_amount

    print("Purchase Amount:", purchase_amount)
    print("Discount:", discount)
    print("Amount Paid:", final_amount)
    print("Wallet Balance:", balance)

except ValueError:
    print("Enter valid numeric values")
except (InvalidPurchaseError, InsufficientBalanceError) as e:
    print(e)
