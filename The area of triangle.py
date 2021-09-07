#Q.3) Python Program to Calculate the Area of a Triangle

a = int(input("side1::"))
b = int(input("side2::"))
c = int(input("side3::"))

s = (a + b + c) / 2 
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is %0.2f' %area)
