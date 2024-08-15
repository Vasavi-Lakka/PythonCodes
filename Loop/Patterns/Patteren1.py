c=int(input())
AC=0
n=1
while True:
    if n>0:
        dummy=n
        summ=0
        L=len(str(dummy))
        while dummy>0:
            rem=dummy%10
            dummy=dummy//10
            summ+=rem**L
        if summ==n:
            print(n)
            AC+=1
    if AC==c:
        break
    n+=1
    
