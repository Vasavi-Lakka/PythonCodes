#to check greatest among 5
a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
if a>b:
    if a>c:
        if a>d:
            if a>e:
                print(a)
            else:
                print(e)
        else:
            if d>e:
                print(d)
            else:
                print(e)
    else:
        if c>d:
            if c>e:
                print(c)
            else:
                print(e)
        else:
            if d>e:
                print(d)
            else:
                print(e)
else:
    if b>c:
        if b>d:
            if b>e:
                print(b)
            else:
                print(e)
        else:
            if d>e:
                print(d)
            else:
                print(e)
    else:
        if c>d:
            if c>e:
                print(c)
            else:
                print(e)
        else:
            if d>e:
                print(d)
            else:
                print(e)
    
                
    
