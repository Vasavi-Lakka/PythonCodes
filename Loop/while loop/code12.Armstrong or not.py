#WAP to check the given number is armstrong or not
n=int(input())
summ=0
dummy=n
L=str(n)
while dummy>0:
    rem=dummy%10
    dummy//=10
    k=rem**len(L)
    summ+=k
#print(summ)
if summ==n:
    print("Armstrong")
else:
    print("Not")

#Execution
'''
1-> Take input from the user
2-> Take dummy input n is initialized with dummy
3-> Take summ=0 asuming that there is no intergers
4-> Convert that input as string to get length
5-> write condition when we need to extarct numbers from the given number we need to do remainder operation
    To extarct individual number and we need to do floor division operation to extract remain values
6-> Take user input as 153
7-> Iteration starts:
    Iteration1: dummy=153>0 condition true and remainder we get 3 and remaining values 15 and k becomes k=5**len(L)
                Length of input is 3 so k becomes 5**3 summ becomes 27.
    Iteration2: dummy=15>0 condition true and remainder we get 5 and remaining values 1 and k becomes k=3**len(L)
                Length of input is 3 so k becomes 3**3 summ becomes 125+27=152
    Iteration3: dummy=1>0 condition true and remainder we get 1 and remaining values 0 and k becomes k=1**len(L)
                Length of input is 3 so k becomes 1**3 summ becomes 152+1=153
    Iteration4: dummy=0>0 condition False doesnt enter into loop comes out from the loop
8-> Checks condition that summ==n condition true
9-> Print the given number 153 is armstrong

'''
