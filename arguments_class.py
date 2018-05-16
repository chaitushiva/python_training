'''Arguments, *args(tuple), **kwargs'''

def my_first_fun(x):
    print(x)

def my_sec_fun(x,*args):
    print "x inside sec_fun:",x
    print "args:",args   #it prints empty tuple
    for each_arg in args:
        print each_arg

def my_third_fun(x,**kwargs):
    print x
    print "kwargs:",kwargs

my_first_fun(10)


my_sec_fun(20,40,50)

my_third_fun(30,a="10",b="20")


