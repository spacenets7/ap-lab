import sqlite3

con = sqlite3.connect(':memory:')
cur = con.cursor()
cur.execute('CREATE TABLE Product (id INTEGER PRIMARY KEY, name TEXT, price REAL, stock INTEGER CHECK(stock >= 0))')
cur.execute('''CREATE TABLE Sale (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER, quantity INTEGER, total REAL,
    FOREIGN KEY(product_id) REFERENCES Product(id))''')
cur.executemany('INSERT INTO Product VALUES (?, ?, ?, ?)', [(1, 'Rice', 60, 5), (2, 'Tea', 25, 3)])
con.commit()

while True:
    choice = input('\n1. Sell  2. Summary  3. Exit: ')
    if choice == '1':
        try:
            product_id = int(input('Product ID: '))
            qty = int(input('Quantity: '))
            con.execute('BEGIN')
            product = cur.execute('SELECT name, price, stock FROM Product WHERE id = ?', (product_id,)).fetchone()
            if product is None:
                raise ValueError('Unknown product ID')
            name, price, stock = product
            if qty <= 0:
                raise ValueError('Quantity must be positive')
            if qty > stock:
                raise ValueError('Insufficient stock')
            cur.execute('UPDATE Product SET stock = stock - ? WHERE id = ?', (qty, product_id))
            cur.execute('INSERT INTO Sale (product_id, quantity, total) VALUES (?, ?, ?)', (product_id, qty, qty * price))
            con.commit()
            print(f'Sale of {qty} {name} committed')
        except (sqlite3.Error, ValueError) as e:
            con.rollback()
            print('Sale rejected:', e)
    elif choice == '2':
        print('Sales summary:')
        for name, qty, total in cur.execute('''SELECT Product.name, SUM(Sale.quantity), SUM(Sale.total)
                                               FROM Sale JOIN Product ON Sale.product_id = Product.id
                                               GROUP BY Product.id, Product.name'''):
            print(f'{name} | Quantity sold: {qty} | Total: {total:g}')
        print('Current stock:')
        for name, stock in cur.execute('SELECT name, stock FROM Product'):
            print(f'{name} | Stock: {stock}')
    elif choice == '3':
        break
    else:
        print('Invalid choice')
con.close()
