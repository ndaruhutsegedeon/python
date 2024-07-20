class student:
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name

        #method

    def display(self):

        print(self.first_name,self.last_name)

#object
my_student=student('john', 'smith')
my_student.display()
my_student2=student('gideon','were')
my_student2.display()


