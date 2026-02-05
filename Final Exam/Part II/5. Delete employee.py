def delete_employees():
    conn = dbCon_employee()
    cursor = conn.cursor()

    emp_id = int(input("Enter Employee ID to delete: "))

    cursor.execute("DELETE FROM employees WHERE id = ?", (emp_id,))
    conn.commit()
    conn.close()

    print("Employee deleted successfully")