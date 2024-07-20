class Employee:
    def __init__(self, name,employee_id,salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_information(self):
        print(f"Name:{self.name}")
        print(f"employee_ID:{self.employee_id}")
        print(f"salary:${self.salary}")

    def calculate_annual_salary(self):
        return self.salary * 12

class manager(Employee):
    def __init_(sef,name,employee_id,salary,department,employees_managed=None):
     super().__init_(name,employee_id,salary)
    self.department = department
    self.employees_managed = employees_managed if employees_managed else[]
    def display_information(self):super().display_information()
    print(f"department:{self.department}")
    print(f"Employess managed:{[employee.name for employee in self.employees_managed]}")
    def add_employee(self,employee):
        self.employees_managed.append(employee)
    def display_employess_managed(self):

    print(f"Employees_managed:") for employee in self.employees_managed:
    print(f"{employee.name}(ID:{employee.employee_id})")

class developer(Employee):
    def __init__(self,name,employee_id,salary,programming_languages=None):
       super()._init_(name,employee_id,salary)
       self.programming_languages=programming_languages if programming_languages else []
    def display_information(self):
           super().display_information()
           print(f"Programming Languages:{.join(self.programming_languages)}")
    def add_programming_language(self,language):
         if language not in self.programming_languages:
         self.programming_languages.append(language)

class intern(employee):
    def __init__(self,name,employee_id,salary,school_name,graduation_year):
        super().__init__(self,name,employee_id,salary)
        self.school_name=school_name
        self.graduation_year=graduation_year
    def display_information(self):
            super().display_information()
         print(f"School name:{self.school_name}")
        print(f"Graduation year:{self.graduation_year}")

#create some employees
manager = Manager("Erick",1,90000"engineering")
developer = Developer("keysha",2,8000,["python","javascript"])
intern=intern("daniel"330000,"state university",2024)
#display their information manager.display_information()
print()
manager.display_information()
developer.display_information()
print()
intern.display_information()
# Manager adds employees to manage
manager.add_employee(developer)
manager.add_employee(intern)
#Display the list of employees managed by the manager
manager.display_employees_managed()

#Developer adds a new programming language
developer.add_programming_language("javascript")
developer.display_information()

#calculate and print annual salaries
print(f"{manager.name}'s Annual Salary:ksh{manager.calculate_annual_salary()}")
print(f"{developer.name}'s Annual Salary:ksh{developer.calculate_annual_salary()}")
print(f"{intern.name}'s Annual Salary:ksh{intern.calculate_annual_salary()}")
