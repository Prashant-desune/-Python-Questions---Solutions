#Q.13)Python Program to Find the Largest Among Three Numbers
a = int(input("number1::"))
b = int(input("number2::"))
c = int(input("number3::"))

if (a>=b) and (a >= c):
    largest = a
elif (b >= a) and (b >= c):
        largest = b
else:
    (c >= a) and (c >= b)
    largest = c 
print("The largest num is :",largest)