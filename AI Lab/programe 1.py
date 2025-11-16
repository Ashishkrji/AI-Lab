# Use logic programming in Python to check for prime numbers.


n=int(input("enter a number"))
if n>=1:
    for i in range(2,n):
        if n%i==0:
            print("Not Prime")
            break
        else:
            print("prime")
else:
    print("Not Prime")