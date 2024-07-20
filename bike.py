class Bike:

    def __init__(self,model,type,color):
        self.model=model
        self.type=type
        self.color=color
     #method
    def display(self):
        print(self.model,self.type,self.color)
#object
my_bike=Bike('Bus','Bus','blue')
my_bike.display()

