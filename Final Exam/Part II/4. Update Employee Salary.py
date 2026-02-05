def update_employee():
    conn, cursor = dbCon_employee()

    emp_id = int(input("Enter Employee ID to update: "))
    salary = float(input("Enter new salary: "))

    cursor.execute(
        "UPDATE employees SET salary=? WHERE id=?",
        (salary, emp_id)
    )

    conn.commit()
    conn.close()
    print("Employee updated successfully")
