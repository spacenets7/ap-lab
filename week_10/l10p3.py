import sqlite3

con = sqlite3.connect(':memory:')
cur = con.cursor()
cur.execute('CREATE TABLE Student (id INTEGER PRIMARY KEY, mark INTEGER CHECK(mark BETWEEN 0 AND 100))')
cur.executemany('INSERT INTO Student VALUES (?, ?)', [(101, 82), (102, 67)])
con.commit()

def show_marks():
    print('Marks:', cur.execute('SELECT * FROM Student ORDER BY id').fetchall())

def update_marks(a, b):
    show_marks()
    try:
        cur.execute('BEGIN')
        cur.execute('UPDATE Student SET mark = ? WHERE id = 101', (a,))
        cur.execute('UPDATE Student SET mark = ? WHERE id = 102', (b,))
        con.commit()
        print('Both updates committed')
    except sqlite3.Error as e:
        con.rollback()
        print('Transaction rolled back:', e)
    show_marks()

print('First attempt')
update_marks(88, 79)
print('Second attempt')
update_marks(95, 120)
con.close()
