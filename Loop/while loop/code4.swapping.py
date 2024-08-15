#WAP to swap the numbers in the list by using while loop
n=eval(input())
i=0
while i<len(n):
    n[i],n[i+1]=n[i+1],n[i]
    i+=2
print(n)

#By using for loop

'''
L=eval(input(())
for ip in range(len(s)):
    if ip%2==0:
        L[ip], L[ip+1]=L[ip+1], L[ip]
print(L)
'''

#Execution
'''
1-> Take input from the user
2-> now initialize variable as a first step or starting index value for while loop i=0
3-> Now write the condition as checking till that conditions becomes false.
4-> if the condition is true then replace or swap 0 index position with 1st index position.
5-> then we need to write the last statements in while loop i+=1
6-> Iteration  Starts: Taking input as [11,22,33,44]
    Iteration1: we initialized i= 0 and checks the condition True enter into while loop now that num swap with
                1st index position number. Now i is incremented by 2 so i=2
    Iteration2: i = 2 and checks the condition True enter into while loop now that num swap with
                3rd index position number. Now i is incremented by 2 so i=5
    Iteration4: i = 5 and checks the condition False doesn't enter into while loop.
7-> Print swaped output as [22,11,44,33]
'''
