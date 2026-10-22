import sqlite3

con = sqlite3.connect(':memory:')
cur = con.cursor()
cur.execute('''CREATE TABLE Book (
    id INTEGER PRIMARY KEY, title TEXT NOT NULL CHECK(TRIM(title) != ''),
    author TEXT, price REAL, quantity INTEGER CHECK(quantity >= 0))''')
cur.executemany('INSERT INTO Book VALUES (?, ?, ?, ?, ?)', [
    (1, 'Python Basics', 'Rao', 450, 5),
    (2, 'SQLite Guide', 'Das', 350, 3),
    (3, 'C Programming', 'Nair', 500, 0)
])

while True:
    print('\n1. Sell  2. List available  3. Delete  4. Exit')
    choice = input('Choice: ')
    if choice == '1':
        book_id = int(input('Book ID: '))
        qty = int(input('Copies sold: '))
        cur.execute('SELECT quantity FROM Book WHERE id = ?', (book_id,))
        book = cur.fetchone()
        if book is None:
            print('Unknown book ID')
        elif qty <= 0 or qty > book[0]:
            print('Invalid quantity or insufficient stock')
        else:
            cur.execute('UPDATE Book SET quantity = quantity - ? WHERE id = ?', (qty, book_id))
            con.commit()
            print('Quantity updated')
    elif choice == '2':
        for title, qty in cur.execute('SELECT title, quantity FROM Book WHERE quantity > 0 ORDER BY title'):
            print(f'{title} | Quantity: {qty}')
    elif choice == '3':
        book_id = int(input('Book ID to delete: '))
        cur.execute('DELETE FROM Book WHERE id = ?', (book_id,))
        print('Book deleted' if cur.rowcount else 'Unknown book ID')
        con.commit()
    elif choice == '4':
        break
    else:
        print('Invalid choice')
con.close()
