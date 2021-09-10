#Q.12)Python Program to Check Leap Year
year = int(input("YEAR::"))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 ==0:
            print(" a leap year")
        else:
            print("not a leap year")
    else:
        print("a leap year")
else:
    print("not a leap year")
    