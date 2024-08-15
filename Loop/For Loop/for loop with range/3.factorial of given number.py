#Factorial of given number
n=int(input())
fact=1
for i in range(1, n+1):
    fact*=i
print(fact)

#Execution
'''
1-> Take input from the user
2-> taking summ=0 assuming that sum as 0
3-> Taking input 5
4-> Iteration starts
    Iteration1:extracts 1 checks condition true fact is 1
    Iteration2:extracts 2 checks condition true fact is 2
    Iteration1:extracts 3 checks condition true fact is 6
    Iteration1:extracts 4 checks condition true fact is 24
    Iteration1:extracts 5 checks condition true fact is 120
5-> print fact as 120'''
    
