# Q.4) Python Program to Solve Quadratic Equation:
import cmath
a = float(input("num1::"))
b = float(input("num2::"))
c = float(input("num3::"))

d = (b**2) - ( 4*a*c )
Quadratic = (-b-cmath.sqrt(d)) / 2*a
Quadratic_1 = (-b+cmath.sqrt(d)) / 2*a
print(Quadratic,Quadratic_1)