#WAP to print the sum of 1st n numbers by using while loop
n=int(input())
summ=0
i=1
while i<=n:
    summ+=i
    i+=1
print(summ)


#Execution
'''
1-> Take input from the user
2-> take summ=0 assuming that total sum as 0
3-> now initialize variable as a first step or starting value for while loop i=1
4-> Now write the condition as checking till that conditions becomes false.
5-> if the condition is true then summ+=i
6-> then we need to write the last statements in while loop i+=1
7-> Iteration  Starts: Taking input as 4
    Iteration1: we initialized i= 1 and checks the condition True enter into while loop summ becomes 1,
                now i becomes 2.
    Iteration2: i = 2 and checks the condition True enter into while loop summ becomes 3,
                i is incremented by 1 now i becomes 3
    Iteration3: i = 3 and checks the condition True enter into while loop summ becomes 6,
                i is incremented by 1 now i becomes 4
    Iteration4: i = 4 and checks the condition True enter into while loop summ becomes 10,
                i is incremented by 1 now i becomes 5
    Iteration4: i = 5 and checks the condition False doesn't enter into while loop summ remains same 10,
8-> Print Summ.
'''
