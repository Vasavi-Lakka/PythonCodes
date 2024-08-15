#WAP to check given number is even or odd by using arithematic operator
a=int(input())
if a%2==0:
    print("EVEN")
else:
    print("ODD")
-----------------------------------
#by using bitwise & and bitwise xor
num=int(input())
if num&1==0:
    print("EVEN")
#if num&1==1:
    #print("ODD")
else:
    print("ODD")
------------------------------------
num=int(input())
if num^1==num+1:
    print("EVEN")
#if num^1==-1:
    #print("ODD")
else:
    print("ODD")

------------------------------
#by using type casting
num=int(input())
s=str(num)
if s[-1] in '02468':
    print('even')
else:
    print('odd')
