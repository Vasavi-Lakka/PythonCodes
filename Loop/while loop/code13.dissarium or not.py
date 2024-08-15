#WAP to print the given number is disarium or not
n=int(input())
summ=0
dummy=n
L=len(str(n))
while dummy>0:
    rem=dummy%10
    dummy//=10
    summ+=rem**L
    L-=1
if summ==n:
    print("Special Number")
else:
    print("Not Specail")

#Execution
'''
1-> Take input from the user
2-> Take summ==0 assuming that sum of its digits is zero
3-> Take dummy=n becoz i dont want to change my actual number
4-> convert that number into string and by using len function we get length of number
5-> Now write the while condition
6-> To get remainder value we need to do modulus operator
7-> To  get remaining values we need to do floor division operation
7-> Iteration Starts:
    
'''

