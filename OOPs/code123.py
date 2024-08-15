'''L='sudha1 yaho5 parvez3 gov2ardhan sra4van'
K=L.split()
A=[]
l=len(K)
#B=''

#print(K)
for i in K:
    A[i]=0
    s=''
    r=' '
    
    for j in v:
        #print(j)
        if j.isalpha():
            s+=j
        else:
            A[i]=j
    

    
        #if j.isdigit():
            #H=j
            
    B+=s+r
    q=B.split()
print(A[i])
if ==H:
        A.append(K[i])
    l+=1
    B+=s+r
print(A)
'''
#M=sorted(H)



#print(B)
#print(sorted(H))
    #print(H)
    #print(s)
































'''L=['sudha1','yaho5','parvez3','gov2ardhan','sra4van']
length=len(L)
summ=0
#a=L[0]
#b=L[1]
for i in range(0,length):
    a=1
    b=2
    k=L[i]
    H=[]
    for j in k:
        if not j.isdigit():
            if j==a:
                print(j)
    
''' 
    












'''
length=len(L)

L.sort()
print(L)

#Z=[]
S=''
for ip in range(0,length):
    K=L[ip]
    #Z.append(K)
    n=''
    Z=[]
    for i in K:
        #Z=[]
        if i.isdigit():
            S+=i
            #S.sort()
            Z.append(S)
              
print(Z)
#print(Z)
      
 '''           
        
        
L = 'sudha1 yaho5 parvez3 gov2ardhan sra4van'
K = L.split()
A = []
h=''
g=len(K)
for i in K:
    s = ''
    m=h[i]
    num = ''
    for j in i:
        if j.isalpha():
            s += j
        else:
            num += j
    if num==m:
        A.append((s, int(num)))
print(A)
'''
# Sort the list of tuples based on the number in ascending order
A.sort(key=lambda x: x[1])

# Create the sorted string without numbers
sorted_L = ' '.join([name for name, num in A])
print(sorted_L)

'''
