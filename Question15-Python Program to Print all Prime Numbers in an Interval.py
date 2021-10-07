#Q.14)Python Program to Print all Prime Numbers in an Interval
lower = int(input("1::"))
upper = int(input("2::"))
for num in range(lower, upper+1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print("The numbers are:: "+str(num))
