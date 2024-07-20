mark = int(input("enter marker:"))

if mark >= 80 and mark <= 100:
    print("you have an A")
elif mark >= 60 and mark <= 70:
    print("you have a B")
elif mark >= 40 and mark <= 59:
    print("you have a C")
elif mark >= 0 and mark <= 39:
    print("you have failed terribly")
else:
    print("wrong inputs,check your marks")

    n1(print("enter first number"))
    n2(print("enter second number"))
    n3(print("enter third number"))
    n4(print("enter the four number"))

if n1 > n2 and n1 > n3 and n1 > n4:
    print(" i am the largest n", n1)
if n2 > n1 and n2 > n3 and n2 > n4:
    print("i am the largest n", n2)
if n3 > n1 and n3 > n2 and n3 > n4:
    print("i am the largest n", n3)
if n4 > n1 and n4 > n2 and n4 > n3:
    print("i am the largest n", n4)
