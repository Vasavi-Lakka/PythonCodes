#WAP to check the given number is perfect or not by using while loop
n=int(input())
ds=0
i=1
while i<=n//2:
    if n%i==0:
        ds+=i
    i+=1
if ds==n:
    print("Is Perfect")
else:
    print("Not Perfect")
        




#Execution
'''
1-> Take input from the user
2-> take fact=1 assuming that 0 factorial is 1
3-> now initialize variable as a first step or starting value for while loop i=1
4-> Now write the condition as checking till that conditions becomes false.
5-> if the condition is true then summ+=i
6-> then we need to write the last statements in while loop i+=1
7-> Iteration  Starts: Taking input as 5
    Iteration1: we initialized i= 1 and checks the condition True enter into while loop fact becomes 1,
                now i becomes 2.
    Iteration2: i = 2 and checks the condition True enter into while loop fact becomes 2,
                i is incremented by 1 now i becomes 3
    Iteration3: i = 3 and checks the condition True enter into while loop fact becomes 6,
                i is incremented by 1 now i becomes 4
    Iteration4: i = 4 and checks the condition True enter into while loop fact becomes 24,
                i is incremented by 1 now i becomes 5
    Iteration5: i = 5 and checks the condition True enter into while loop fact becomes 120,
                i is incremented by 1 now i becomes 6
    Iteration4: i = 6 and checks the condition False doesn't enter into while loop fact remains same 120,
8-> Print fact as 120.
'''
