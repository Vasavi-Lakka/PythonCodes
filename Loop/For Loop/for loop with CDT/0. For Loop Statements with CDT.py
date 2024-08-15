#For loop with sting:
s='vasavi'
for i in s:#checking iterations using for loop
    print(i)

#-------------------====
#for loop with empty string:

s1=''
for i in s1:
    print(i)#retruns Nothing
#----------------------------------
#for loop with list
L=[11,22,44,'hello',[1,2]]
for i in L:
    print(i)

#---------------------------------
#for loop with tuples
T=[11,22,44,['hello'],(1,2)]
for i in T:
    print(i)

#-----------------------------------
#for loop with set
s={11,22,44,'hello',(1,2)}
for i in s:
    print(i)#returns values in random order
#--------------------------------------------
#for loop with dict
d={'Greet':'hello', 'name':'Vasu', 'age':22}
for i in d:
    print(i)#returns only keys

d={'Greet':'hello', 'name':'Vasu', 'age':22}
for i in d:
    print(i,d[i])#returns keys and values

d={'Greet':'hello', 'name':'Vasu', 'age':22}
for i in d:
    print(d[i])#returns only values


#for loop with dictionary items methods
#we need to use two variables as data is represented in key value pairs

d={'Greet':'hello', 'name':'Vasu', 'age':22}
for i,j in d.items():
    print(i,j)#returns both keys and values





    
