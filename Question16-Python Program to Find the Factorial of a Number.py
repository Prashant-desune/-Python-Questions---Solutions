#Q.15)Python Program to Find the Factorial of a Number
num = int(input("number::"))
fact = 1 
if num < 0:
    print("not possible")
elif num == 0:
    print("factorial of zero is always 1")
else:
    for i in range(1, num+1):
        fact = fact * i 
    print('The factorial of',num, "is:",fact)