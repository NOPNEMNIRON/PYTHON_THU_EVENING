#Update a student's course by StudentID
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
