# Employee Management System
## Description
The Employee Management System is a Python CLI application that allows users to manage employees and their departments. This system includes functionalities to add, delete, and view employees and departments, along with assigning employees to specific departments.

### Features
Add, delete, and view employees.
Add, delete, and view departments.
Assign employees to departments.
View employees by department.
Comprehensive input validation and error handling.
Project Structure
markdown
Copy code
employee_management_system/
│
├── README.md
├── Pipfile
├── main.py
├── models/
│   ├── __init__.py
│   ├── department.py
│   └── employee.py
├── cli/
│   ├── __init__.py
│   ├── menu.py
│   └── utils.py
└── database/
    ├── __init__.py
    └── setup.py
## Setup and Installation
### Clone the repository:

sh
Copy code
git clone https://github.com/yourusername/employee_management_system.git
cd employee_management_system
### Set up the virtual environment:
pipenv install

### Activate the virtual environment:
pipenv shell


# Usage

### Run the application:

python employeemanagementsystem.py

### Follow the on-screen menu options to manage employees and departments:

Main Menu
Add a Employee
Remove a Employee
Promote a Employee
Display a Employee


Displays a list of all employees with their respective details.
Models
Department
id: Primary Key
name: String (unique, not null)
description: String (optional)
Employee
id: Primary Key
name: String (not null)
email: String (unique, not null)
department_id: Foreign Key referencing Department.id

# ORM Methods
Department
Create
Delete
Get all
Find by ID
Employee
Create
Delete
Get all
Find by ID
Error Handling
Validates user inputs (e.g., ensures non-empty strings, valid email format).
Provides informative error messages for invalid inputs or actions (e.g., trying to delete a non-existent record).

# Contributing
## Fork the repository.
Create your feature branch (git checkout -b feature/AmazingFeature).
Commit your changes (git commit -m 'Add some AmazingFeature').
Push to the branch (git push origin feature/AmazingFeature).
Open a Pull Request.

# License
This project is licensed under the MIT License - see the LICENSE file for details.

Contact
Your Name - @your_twitter - your_email@example.com

Project Link: https://github.com/yourusername/employee_management_system


