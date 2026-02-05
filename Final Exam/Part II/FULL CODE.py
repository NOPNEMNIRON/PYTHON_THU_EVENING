import sqlite3

# 1. Database connection function
def dbCon_employee():
    conn = sqlite3.connect("employee.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            position TEXT,
            salary INTEGER
        )
    """)
    conn.commit()
    return conn


# 2. Add employee
def add_employee():
    conn = dbCon_employee()
    cursor = conn.cursor()

    name = input("Enter name: ")
    position = input("Enter position: ")
    salary = int(input("Enter salary: "))

    cursor.execute(
        "INSERT INTO employees (name, position, salary) VALUES (?, ?, ?)",
        (name, position, salary)
    )
    conn.commit()
    conn.close()

    print("Employee added successfully")


# 3. View employees
def view_employees():
    conn = dbCon_employee()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM employees")
    records = cursor.fetchall()

    print("\nID | Name | Position | Salary")
    print("--------------------------------")
    for row in records:
        print(row)

    conn.close()


# 4. Update employee
def update_employee():
    conn = dbCon_employee()
    cursor = conn.cursor()

    emp_id = int(input("Enter Employee ID to update: "))
    new_salary = int(input("Enter new salary: "))

    cursor.execute(
        "UPDATE employees SET salary = ? WHERE id = ?",
        (new_salary, emp_id)
    )
    conn.commit()
    conn.close()

    print("Employee updated successfully")


# 5. Delete employee
def delete_employees():
    conn = dbCon_employee()
    cursor = conn.cursor()

    emp_id = int(input("Enter Employee ID to delete: "))

    cursor.execute("DELETE FROM employees WHERE id = ?", (emp_id,))
    conn.commit()
    conn.close()

    print("Employee deleted successfully")


# 6. Menu driven function
def manu():
    while True:
        print("\n===== Employee Management System =====")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Exit")

        choice = input("Enter choice (1-5): ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            update_employee()
        elif choice == "4":
            delete_employees()
        elif choice == "5":
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice")
manu()