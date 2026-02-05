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