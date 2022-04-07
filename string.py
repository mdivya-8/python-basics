#STRINGS: collection of characters enclosed by double quotes.
#single quotes:'this is python'
#DOUBLE QUOTES:"this is python coding"
#multi lin equotes: """this is python training session."""

a="banana"
b="apple"
print(a + b)
print(id(a))
print(id(b))
print(id(a)+id(b))

#a.append("mango")
#print(a)

c=a.upper()   #upper()
print(c)

d=a.count(a)#count()
print(d)

string="mango","alpha","gamma"
print(string[1])  #index()
'''string1=a.expand(2)
print(string1)'''
print(len(string)) #length()

m="UPPER"
print(m)
n=m.lower()  #lower()
print(n)

name="my  \'fav name is' \'divya' " # escape sequence
print(name)

name1="divya"
print(name1[1])   #index
for i in name1:
    print(i)
name1.capitalize() #divya

string="hi {},good {}"
str=string.format("all","evening")#format
