products = {}
categories = set()
sales = []

while True:
    print("\n1. Add Product\n2. Search Product\n3. Purchase Product\n4. Display Products\n5. Display Categories\n6. Low Stock Report\n7. Sales Summary\n8. Exit")
    ch = input("Enter choice: ")

    if ch == "1":
        pid = input("Product ID: ")
        if pid in products:
            print("Duplicate Product ID")
            continue
        name = input("Product Name: ")
        category = input("Category: ")
        price = float(input("Price: "))
        qty = int(input("Quantity: "))
        products[pid] = ((name, category, price), qty)
        categories.add(category)

    elif ch == "2":
        pid = input("Product ID: ")
        if pid in products:
            print(pid, products[pid])
        else:
            print("Product not found")

    elif ch == "3":
        pid = input("Product ID: ")
        if pid not in products:
            print("Product not found")
            continue
        qty = int(input("Quantity: "))
        details, stock = products[pid]
        if qty <= 0 or qty > stock:
            print("Insufficient quantity")
            continue
        name, category, price = details
        amount = qty * price
        products[pid] = (details, stock - qty)
        sales.append((pid, name, qty, amount))
        print("Purchase successful")

    elif ch == "4":
        for pid, (details, qty) in products.items():
            print(pid, details, qty)

    elif ch == "5":
        print(categories)

    elif ch == "6":
        for pid, (details, qty) in products.items():
            if qty < 5:
                print(pid, details, qty)

    elif ch == "7":
        total = sum(s[3] for s in sales)
        print("Total sales:", total)
        if sales:
            top = max(sales, key=lambda x: x[3])
            print("Highest sales product:", top[1], top[3])

    elif ch == "8":
        break

    else:
        print("Invalid choice")
