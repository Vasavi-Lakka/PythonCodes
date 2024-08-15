LL=int(input("enter num1"))
UL=int(input("enter num21"))
for n in range(LL,UL+1):
    dummy=n
    summ=0
    while dummy>0:
        rem=dummy%10
        dummy//=10
        fact=1
        for i in range(1,rem+1):
            fact*=i
        summ+=fact
    if n==summ:
        print("special")
        print(n)
