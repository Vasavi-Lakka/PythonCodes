d={'a':10,'b':20,'c':40}
d1={'a':20,'b':35,'c':35,'d':45}
d2={}
'''if d['a']>d1['c']:
    add.d2(d['a'])
else:
    add.d2(d1['a'])'''
'''K=list(d)
L=list(d1)
Z=update.d2(d1,d)
print(Z)
'''
#k=set(d.items()).union(set(d1.items()))
#print(k)'''
s=list(d)+list(d1)
for key in s:
    if d.get(key,0)>d1.get(key,0):
        d2[key]=d.get(key,0)
    else:
        d2[key]=d1.get(key,0)
print(d2)
