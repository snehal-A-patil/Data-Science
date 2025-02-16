import sys

def main_menu():
    employees = {
        101: {'name': 'Satya', 'age': 27, 'department': 'HR', 'salary': 50000},
        102: {'name': 'Snehal', 'age': 20, 'department': 'IT', 'salary': 60000}
    }
    
    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search for Employee")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_employee(employees)
        elif choice == '2':
            view_employees(employees)
        elif choice == '3':
            search_employee(employees)
        elif choice == '4':
            print("Thank you for using the Employee Management System. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please enter a valid option.")

def add_employee(employees):
    try:
        emp_id = int(input("Enter Employee ID: "))
        if emp_id in employees:
            print("Employee ID already exists. Please enter a unique ID.")
            return
        name = input("Enter Employee Name: ")
        age = int(input("Enter Employee Age: "))
        department = input("Enter Employee Department: ")
        salary = float(input("Enter Employee Salary: "))
        
        employees[emp_id] = {'name': name, 'age': age, 'department': department, 'salary': salary}
        print("Employee added successfully!")
    except ValueError:
        print("Invalid input. Please enter correct details.")

def view_employees(employees):
    if not employees:
        print("No employees available.")
        return
    print("\nEmployee Details")
    print("ID\tName\tAge\tDepartment\tSalary")
    print("-" * 40)
    for emp_id, details in employees.items():
        print(f"{emp_id}\t{details['name']}\t{details['age']}\t{details['department']}\t{details['salary']}")

def search_employee(employees):
    try:
        emp_id = int(input("Enter Employee ID to search: "))
        if emp_id in employees:
            details = employees[emp_id]
            print("\nEmployee Found:")
            print(f"ID: {emp_id}, Name: {details['name']}, Age: {details['age']}, Department: {details['department']}, Salary: {details['salary']}")
        else:
            print("Employee not found.")
    except ValueError:
        print("Invalid input. Please enter a valid Employee ID.")

if __name__ == "__main__":
    main_menu()
