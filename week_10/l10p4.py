import sqlite3

con = sqlite3.connect(':memory:')
cur = con.cursor()
cur.execute('CREATE TABLE Account (id INTEGER PRIMARY KEY, name TEXT, balance REAL CHECK(balance >= 0))')
cur.executemany('INSERT INTO Account VALUES (?, ?, ?)', [(1001, 'Asha', 5000), (1002, 'Ravi', 2000)])
con.commit()

def balances():
    for account_id, name, balance in cur.execute('SELECT * FROM Account ORDER BY id'):
        print(f'{account_id} | {name} | Balance: {balance:.2f}')

while True:
    print('\nADD / DEPOSIT / WITHDRAW / TRANSFER / EXIT')
    choice = input('Choice: ').upper()
    if choice == 'EXIT':
        break
    try:
        if choice == 'ADD':
            account_id = int(input('ID: '))
            name = input('Name: ')
            amount = float(input('Opening balance: '))
            if not name.strip() or amount < 0:
                raise ValueError('Invalid account details')
            cur.execute('INSERT INTO Account VALUES (?, ?, ?)', (account_id, name, amount))
        elif choice in ('DEPOSIT', 'WITHDRAW'):
            account_id = int(input('Account ID: '))
            amount = float(input('Amount: '))
            account = cur.execute('SELECT balance FROM Account WHERE id = ?', (account_id,)).fetchone()
            if account is None or amount <= 0:
                raise ValueError('Unknown account or invalid amount')
            if choice == 'WITHDRAW' and account[0] < amount:
                raise ValueError('Insufficient funds')
            change = amount if choice == 'DEPOSIT' else -amount
            cur.execute('UPDATE Account SET balance = balance + ? WHERE id = ?', (change, account_id))
        elif choice == 'TRANSFER':
            source = int(input('From account: '))
            target = int(input('To account: '))
            amount = float(input('Amount: '))
            con.execute('BEGIN')
            a = cur.execute('SELECT balance FROM Account WHERE id = ?', (source,)).fetchone()
            b = cur.execute('SELECT balance FROM Account WHERE id = ?', (target,)).fetchone()
            if a is None or b is None or source == target or amount <= 0:
                raise ValueError('Invalid accounts or amount')
            if a[0] < amount:
                raise ValueError('Insufficient funds')
            cur.execute('UPDATE Account SET balance = balance - ? WHERE id = ?', (amount, source))
            cur.execute('UPDATE Account SET balance = balance + ? WHERE id = ?', (amount, target))
        else:
            print('Invalid choice')
            continue
        con.commit()
        print('Operation committed')
    except (sqlite3.Error, ValueError) as e:
        con.rollback()
        print('Operation rejected:', e)
    balances()
con.close()
