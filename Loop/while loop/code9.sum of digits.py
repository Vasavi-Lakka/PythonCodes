#WAP to print sum of indidvidual digits of a given number
n=int(input())
summ=0
while n>0:
    rem=n%10
    n=n//10
    summ+=rem

print(summ)

#Execution
'''
1-> Take input from the user
2-> Take summ=0 asuming that summ of indidvidual digits sum is 0
3-> Now we need to write condition as that Till that condition becomes False
4-> Now we need to extrat evary individual number by using remainder operation
5-> Now to get remaining values we need to do floor division operation.
6-> Take user input as 457
7-> Iteration starts:
    Iteration-1: n=457 checks condition true enters into while block do's operation remainder we get 7
                 and remaining values we get 45, Now summ becomes 7
    Iteration-2: n=45 checks condition true enters into while block do's operation remainder we get 5
                 and remaining values we get 4, Now summ becomes 7+5 =12
    Iteration-3: n=4 checks condition true enters into while block do's operation remainder we get 4
                 and remaining values we get 0, Now summ becomes 12+4=16
    Iteration-4: n=0 checks condition False doesn't enter into while loop.
8-> Print output as summ 16
'''
