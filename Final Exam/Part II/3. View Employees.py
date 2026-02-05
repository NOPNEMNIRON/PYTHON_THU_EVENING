def view_employees():
    conn, cursor = dbCon_employee()
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()

    print("\nID | Name | Position | Salary")
    print("--------------------------------")
    for row in rows:
        print(row)

    conn.close()
