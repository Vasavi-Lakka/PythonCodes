def divide_without_error(arg):
    def inner(a,b):
        if b!=0:
            arg(a,b)
        else:
            arg(b,a)
    return inner
@divide_without_error
def division(a,b):
    print(a/b)
division(10,2)#5.0
division(10,0)#0.0
