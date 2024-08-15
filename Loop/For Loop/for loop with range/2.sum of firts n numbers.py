#print sum of first n numbers 
n=int(input())
summ=0
for i in range(1, n+1):
    summ+=i
print(summ)

#Execution
'''
1-> Take input from the user
2-> taking summ=0 assuming that sum as 0
3-> Taking input 4
4-> Iteration starts
    Iteration1:extracts 1 checks condition true sum is 1
    Iteration2:extracts 2 checks condition true sum is 3
    Iteration3:extracts 3 checks condition true sum is 6
    Iteration4:extracts 4 checks condition true sum is 10
5-> Print sum as 10'''
