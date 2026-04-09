import sqlite3

# Connect to a database (creates it if it doesn’t exist)
conn = sqlite3.connect('students.db')
cursor = conn.cursor()

# Create a table
cursor.execute('CREATE TABLE IF NOT EXISTS students (id INTEGER, name TEXT)')

# Insert a new student
cursor.execute('INSERT INTO students (id, name) VALUES (?, ?)', (1, 'Alice'))

# Get all students
cursor.execute('SELECT * FROM students')
students = cursor.fetchall()

print(students)  # Output: [(1, 'Alice')]

# Close the connection
conn.close()


