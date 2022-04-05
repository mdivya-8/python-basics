a=10
print(a)

a="hello world"
print(a)

a=b=c=5
print(a,b,c)

a,b,c,d=10,20.5,"Python",True
print(a,b,c,d)

a,b,c,d=10,20.5,"python",True
print(d,c,b,a)

txt="my name is{fname},i'm{age}years old.".format(fname="dolly",age=2)
txt="my name is{0},i'm {1}years old.".format("dolly",2)
txt="my name is{},i'm {}years old.".format("dolly",2)

def m1():
    a=10     #local to m1
    print(a)
    return
def m2():
    a=20    #local to m2
    print(a)
    return
m1()
m2()

def m1():
    a=10     #local to m1
    print(a)
    return
def m2(a):
    a=20    #local to m2
    print(a)
    return
m1()
m2(20)

a=20
def test():
    global a
    a=a+10
    print(a)
    return
test()
print(a)

a=20
b=10
c=15
d=5
e=0
e=(a+b)*c/d
print(e)

x=10
print(id(x))
print(id(10))
print(id(9+1))
print(id(2*5))
print(id(8+2))
y='python'
print(id(y))
print(id('python'))

for i in range(6):
    print(i)

for i in range(1,6):
    print(i)
    
for i in range(-6):   # it doesnt goes from highest to lowest
    print(i)
    
for i in range(-2,-6): # it doesnt goes from highest to lowest
    print(i)
    
for i in range(-6,-2):   # it  goes from highest to lowest
    print(i)
    
for i in range(-6,3):   # it  goes from highest to lowest
    print(i)

for i in range(2,20,3):
    print(i)



    
