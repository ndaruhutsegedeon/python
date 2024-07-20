


class cars:
    def __init__(self,model ,year_of_manufacturing,type,color):
         self.model = model
         self.year_of_manufacturing = year_of_manufacturing
         self.type = type
         self.color = color

    #method

    def display(self):
        print(f" my nice {self.model} is {self.year_of_manufacturing} in year of manufacturing and is  {self.type} and have a {self.color}" )

        #object

my_cars=cars('benz','1995','new model','black')
my_cars.display()

