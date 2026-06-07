import sqlite3

con = sqlite3.connect("project.db")
cursor = con.cursor()

# Create table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        grade TEXT NOT NULL
    )
""")

# Insert some data
cursor.execute("INSERT INTO students (name, age, grade) VALUES ('Ali', 20, 'A')")
cursor.execute("INSERT INTO students (name, age, grade) VALUES ('Sara', 22, 'B')")
cursor.execute("INSERT INTO students (name, age, grade) VALUES ('Ahmed', 21, 'A')")

con.commit()

# Read and print data
print("All Students:")
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
for row in rows:
    print(f"ID: {row[0]} | Name: {row[1]} | Age: {row[2]} | Grade: {row[3]}")

con.close()
print("Done!")