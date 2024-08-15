# Sum of integers in a given string
s=input()
sum=0
for i in s:
    if i.isdigit():
        k=int(i)
        sum+=print(sum)


#Execution
'''1-> Take input from the user
2-> take sum=0 assuming that sum of integers in a given string is 0
3-> take inputs as 12Va34
4-> Iteration starts
    Iteration-1: extarcts 1 and checks condition true and converts into int and now sum is 1
    Iteration-2: extarcts 2 and checks condition true and converts into int and now sum is 3
    Iteration-3: extarcts V and checks condition False and sum remains 3
    Iteration-4: extarcts a and checks condition False and sum remains 3
    Iteration-5: extarcts 3 and checks condition true and converts into int and now sum is 6
    Iteration-6: extarcts 4 and checks condition true and converts into int and now sum is 10
5-> Prints sum as 10'''
    
