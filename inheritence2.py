class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def print_name(self):
        print(f"My name is {self.first_name}, {self.last_name},and am {self.age} year old")


class Student(Person):
    def __init__(self, first_name, last_name, age, ):
        super().__init__(first_name,last_name,age)

my_Student = Student("John", "Doe", 23)
my_Student.print_name()

my_Student2 = Student("gideon", "joel", 30)
my_Student2.print_name()

my_Student3 = Student("hamza", "shabbil", 40)
my_Student3.print_name()
