
def calculate():

    num1=int(input("Enter first number: "))
    operator=input(",+,%,*,/-,: ")

    num2=int(input("Enter second number: "))

    num3=int(input("enter third number"))
    operator=input("/,+,-,*,%")
    num4=int(input("enter fourth number"))

    if operator=="+":
        print(num3+num4)

    if operator == "+":

        print(num1+num2)

    if operator == "-":
        print(num1-num2)
    if operator == "*":
      print(num1*num2)
    if operator == "/" :
     print(num1 / num2 )

    if operator == "%":
      print(num1 %num2)


calculate()