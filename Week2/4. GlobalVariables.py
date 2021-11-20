a=300
def func():
    a=3 # this is local. Both the a is different
func()
print(a)


a1=300
def GlobalFunc():
    global a1
    a1=3 # now this is the global a
func()
print(a1)