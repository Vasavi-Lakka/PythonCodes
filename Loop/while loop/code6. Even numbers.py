#WAP to print even numbers
LL=int(input())
UL=int(input())
i=LL
while i<=UL:
    if i%2==0:
        print(i)
    i+=1


#Execution
'''
1-> Take input from the user lower limit.
2-> Take input from the user upper limit.
3-> we need to initialize variable as 1st starting value i=lower limit
4-> Now write the condition as checking till that conditions becomes false.
5-> taking input from the user as LL as 1 and UL as 6
6-> Iteration starts:
    Iteration1-> i=1 checks while condition True enters into block checks if condition False 
                 doesnt enter into if block now i is incremented by 1.
    Iteration2-> i=2 checks while condition True enter into block checks if condition True enters
                 into if block prints 2 and i is incremented by 1
    Iteration3-> i=3 checks while condition True enters into block checks if condition False 
                 doesnt enter into if block now i is incremented by 1.
    Iteration4-> i=4 checks while condition True enter into block checks if condition True enters
                 into if block prints 4 and i is incremented by 1
    Iteration5-> i=5 checks while condition True enters into block checks if condition False 
                 doesnt enter into if block now i is incremented by 1.
    Iteration6-> i=6 checks while condition True enter into block checks if condition True enters
                into if block prints 6 and i is incremented by 1
    Iteration7-> i=7 checks while condition False
7-> Print Even numbers 2
                       4
                       6.
'''
    
