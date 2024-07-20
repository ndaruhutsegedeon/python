class watu:
    def __init__(self,name,age,height,weight):
        self.name=name
        self.age=age
        self.height=height
        self.weight=weight

        #method

    def display(self):

        print(self.name, self.age, self.height, self.weight)

#object

my_watu=watu('watu','25','25','25')
my_watu.display()
my_watu2=watu('watu','25','25','25')