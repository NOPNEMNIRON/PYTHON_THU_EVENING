# 1. Create a text file
with open("students.txt", "w") as file:
    file.write("Molyka\n")
    file.write("Gechh\n")
    file.write("Ricky\n")
    file.write("Neymar\n")
    file.write("Jacky\n")

print("students.txt file created successfully.")

# 2. Count total number
with open("students.txt", "r") as file:
    lines = file.readlines()

total_lines = len(lines)
total_words = sum(len(line.split()) for line in lines)

print("Total lines:", total_lines)
print("Total words:", total_words)

# 3. Search for a specific word
word = input("Enter word to search: ")

with open("students.txt", "r") as file:
    content = file.read()

if word in content:
    print("Word exists in the file.")
else:
    print("Word does not exist in the file.")

# 4. Python to MS Access
import sqlite3

conn = sqlite3.connect("school.db")
print("Connected to database successfully")
conn.close()

# 5. Create Students table
import sqlite3

conn = sqlite3.connect("school.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Students (
    StudentID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT,
    Age INTEGER,
    Course TEXT
)
""")

conn.commit()
conn.close()
print("Students table created successfully")

# 6.Insert student record
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

# 7. View Records
import sqlite3

conn = sqlite3.connect("school.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM Students")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()

# 8. #Update a student's course by StudentID
import sqlite3

conn = sqlite3.connect("school.db")
cursor = conn.cursor()

sid = int(input("Enter StudentID: "))
course = input("Enter new course: ")

cursor.execute(
    "UPDATE Students SET Course=? WHERE StudentID=?",
    (course, sid)
)

conn.commit()
conn.close()
print("Student updated successfully")

#Deletes a student record by StudentID
import sqlite3

conn = sqlite3.connect("school.db")
cursor = conn.cursor()

sid = int(input("Enter StudentID to delete: "))
cursor.execute("DELETE FROM Students WHERE StudentID=?", (sid,))

conn.commit()
conn.close()
print("Student deleted successfully")
