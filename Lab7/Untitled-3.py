class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def get_info(self):
        return f"Employee Name: {self.name}, ID: {self.emp_id}"

class Manager(Employee):
    def __init__(self, name, emp_id, department):
        super().__init__(name, emp_id)
        self.department = department

    def manage_project(self):
        return f"Manager {self.name} is managing a project in the {self.department} department."

class Technician(Employee):
    def __init__(self, name, emp_id, specialization):
        super().__init__(name, emp_id)
        self.specialization = specialization

    def perform_maintenance(self):
        return f"Technician {self.name} is performing maintenance in the field of {self.specialization}."

class TechManager(Manager, Technician):
    def __init__(self, name, emp_id, department, specialization):
        # Initialize both Manager and Technician explicitly
        Manager.__init__(self, name, emp_id, department)  # Initialize Manager part
        Technician.__init__(self, name, emp_id, specialization)  # Initialize Technician part
        self.team = []  # Team list to hold team members

    def add_employee(self, employee):
        self.team.append(employee)

    def get_team_info(self):
        if not self.team:
            return "No team members."
        return "\n".join([emp.get_info() for emp in self.team])

# Create employees of different types
emp1 = Employee("Mikhail", 1)
manager = Manager("Aleksandr", 2, "Sales")
technician = Technician("Dmitriy", 3, "Electrical")
tech_manager = TechManager("Ivan", 4, "IT", "software dev")

# Demonstrate functionality of each class
print(emp1.get_info())  # Print basic employee info
print(manager.get_info())  # Print manager info
print(manager.manage_project())  # Manager manages project

print(technician.get_info())  # Technician info
print(technician.perform_maintenance())  # Technician performs maintenance

# TechManager can manage projects and perform technical tasks
print(tech_manager.get_info())  # TechManager info
print(tech_manager.manage_project())  # TechManager manages project
print(tech_manager.perform_maintenance())  # TechManager performs maintenance

# Add employees to TechManager's team
tech_manager.add_employee(emp1)
tech_manager.add_employee(manager)
tech_manager.add_employee(technician)

# Get team info
print("Team Info:")
print(tech_manager.get_team_info())
