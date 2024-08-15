#WAP to swap the numbers in the list
n=eval(input())
for i in range(len(n)):
    if i%2==0:
        n[i],n[i+1]=n[i+1],n[i]
print(n)
