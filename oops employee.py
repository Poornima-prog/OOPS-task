#Employee
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_salary(self):
        return self.salary


# RegularEmployee
class RegularEmployee(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def calculate_salary(self):
        return self.salary + self.bonus


#ContractEmployee
class ContractEmployee(Employee):
    def __init__(self, name, salary, contract_duration):
        super().__init__(name, salary)
        self.contract_duration = contract_duration

    def calculate_salary(self):
        return self.salary * self.contract_duration


# Manager
class Manager(Employee):
    def __init__(self, name, salary, department, incentive):
        super().__init__(name, salary)
        self.department = department
        self.incentive = incentive

    def calculate_salary(self):
        return self.salary + self.incentive


regular_employee = RegularEmployee("John", 3000, 500)
contract_employee = ContractEmployee("Jane", 4000, 0.5)
manager = Manager("Alice", 6000, "HR", 1000)

print(f"Regular Employee Salary: {regular_employee.calculate_salary()}")
print(f"Contract Employee Salary: {contract_employee.calculate_salary()}")
print(f"Manager Salary: {manager.calculate_salary()}")
