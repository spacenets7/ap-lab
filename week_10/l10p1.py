import sqlite3

con = sqlite3.connect(':memory:')
cur = con.cursor()
cur.execute('CREATE TABLE Student (id INTEGER, name TEXT, department TEXT, mark INTEGER)')
cur.executemany('INSERT INTO Student VALUES (?, ?, ?, ?)', [
    (1, 'A', 'CSE', 80), (2, 'B', 'CSE', 90),
    (3, 'C', 'ECE', 70), (4, 'D', 'ECE', 76),
    (5, 'E', 'IT', 82), (6, 'F', 'IT', 86)
])

print('Department | Students | Average | Highest | Lowest')
cur.execute('''SELECT department, COUNT(*), AVG(mark), MAX(mark), MIN(mark)
               FROM Student GROUP BY department
               HAVING AVG(mark) >= 75 ORDER BY AVG(mark) DESC''')
for dept, count, avg, high, low in cur.fetchall():
    print(f'{dept} | {count} | {avg:.2f} | {high} | {low}')
con.close()
