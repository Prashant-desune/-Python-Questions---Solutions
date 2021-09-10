#Q.14)Python Program to Check Prime Number
num = int(input("number::"))
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("not Prime number")
            break
    else:
        print("prime number")
else:
    print("not prime number")
    


#Q.14)Python Program to Check Prime Number flag
num = int(input("number::"))
flag = False
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            flag = True
            break
if flag:
    print("not prime")
else:
    print("prime")