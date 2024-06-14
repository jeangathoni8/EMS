import mysql.connector

# Function to establish database connection
def connect_to_database():
    try:
        con = mysql.connector.connect(
            host='localhost',
            port='3306',
            user='root',
            password='password',
            database='emp'
        )
        return con
    except mysql.connector.Error as e:
        print(f"Error connecting to database: {e}")
        return None

# Function to create database and table
def create_database_and_table(con):
    try:
        cursor = con.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS emp")
        cursor.execute("USE emp")
        cursor.execute("CREATE TABLE IF NOT EXISTS empd (id INT PRIMARY KEY, name VARCHAR(255), post VARCHAR(255), salary DECIMAL)")
        con.commit()
        print("Database and table created successfully")
    except mysql.connector.Error as e:
        print(f"Error creating database/table: {e}")

# Function to add an employee
def add_employee(con):
    try:
        cursor = con.cursor()
        id = int(input("Enter Employee Id : "))
        name = input("Enter Employee Name : ")
        post = input("Enter Employee Post : ")
        salary = float(input("Enter Employee Salary : "))
        cursor.execute("INSERT INTO empd (id, name, post, salary) VALUES (%s, %s, %s, %s)", (id, name, post, salary))
        con.commit()
        print("Employee added successfully")
    except mysql.connector.Error as e:
        print(f"Error adding employee: {e}")

# Function to remove an employee
def remove_employee(con):
    try:
        cursor = con.cursor()
        id = int(input("Enter Employee Id to remove: "))
        cursor.execute("DELETE FROM empd WHERE id = %s", (id,))
        con.commit()
        print("Employee removed successfully")
    except mysql.connector.Error as e:
        print(f"Error removing employee: {e}")

# Function to promote an employee
def promote_employee(con):
    try:
        cursor = con.cursor()
        id = int(input("Enter Employee Id to promote: "))
        amount = float(input("Enter increase in Salary: "))
        cursor.execute("SELECT salary FROM empd WHERE id = %s", (id,))
        current_salary = cursor.fetchone()[0]
        new_salary = current_salary + amount
        cursor.execute("UPDATE empd SET salary = %s WHERE id = %s", (new_salary, id))
        con.commit()
        print("Employee promoted successfully")
    except mysql.connector.Error as e:
        print(f"Error promoting employee: {e}")

# Function to display all employees
def display_employees(con):
    try:
        cursor = con.cursor()
        cursor.execute("SELECT * FROM empd")
        employees = cursor.fetchall()
        for employee in employees:
            print("Employee Id:", employee[0])
            print("Employee Name:", employee[1])
            print("Employee Post:", employee[2])
            print("Employee Salary:", employee[3])
            print("---------------------")
    except mysql.connector.Error as e:
        print(f"Error displaying employees: {e}")

# Main menu function
def menu(con):
    while True:
        print("\nWelcome to Employee Management Record")
        print("1. Add Employee")
        print("2. Remove Employee")
        print("3. Promote Employee")
        print("4. Display Employees")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_employee(con)
        elif choice == '2':
            remove_employee(con)
        elif choice == '3':
            promote_employee(con)
        elif choice == '4':
            display_employees(con)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

# Main function
def main():
    con = connect_to_database()
    if con:
        create_database_and_table(con)
        menu(con)
        con.close()

if __name__ == "__main__":
    main()
