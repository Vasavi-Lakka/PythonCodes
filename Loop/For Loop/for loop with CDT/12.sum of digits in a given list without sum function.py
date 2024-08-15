#sum of integers in a given list
L=eval(input())
summ=0
for k in L:
    if isinstance(k, int):
        summ+=k
print(summ)
'''
1-->List of only integers
L=eval(input())
summ=0
for i in L:
    summ+=i
print(summ)

2------>in one line by using sum function when list contains numbers
L=eval(input())
print(sum(L))''''

#Execution
'''
1-> Take input from the user
2-> take summ=0 assuming that there is no instegers in a given list
3-> Taking input as [1, 2,'hai',3]
4-> Iteration starts
    Iteration1: extracts 1 and checks the condition True summ becomes 1
    Iteration2: extracts 2 and checks the condition True summ becomes 3
    Iteration3: extracts 'hai' and checks the condition false summ remains 3
    Iteration4: extracts 3 and checks the condition True summ becomes 6
5-> Prints sum of int as 6'''
    
