import sqlite3

conn = sqlite3.connect("school.db")
cursor = conn.cursor()

name = input("Enter name: ")
age = int(input("Enter age: "))
course = input("Enter course: ")

cursor.execute(
    "INSERT INTO Students (Name, Age, Course) VALUES (?, ?, ?)",
    (name, age, course)
)

conn.commit()
conn.close()
print("Student inserted successfully")
