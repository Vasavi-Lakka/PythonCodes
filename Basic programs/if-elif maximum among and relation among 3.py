#Greatest among 3
a=int(input())
b=int(input())
c=int(input())
if a>b and a>c:
    print(a)
elif b>c:
    print(b)
else:
    print(c)
------------------------------
#relation amomg3
a=int(input())
b=int(input())
c=int(input())
if a==b==c:
    print("all are equal")
elif a>b and a>c:
    print(a)
elif b>c:
    print(b)
else:
    print(c)
----------------------------------
#greatest among4
a=int(input())
b=int(input())
c=int(input())
d=int(input())
if a>b and a>c and a>d:
    print(a)
elif b>c and b>d:
    print(b)
elif c>d:
    print(c)
else:
    print(d)
