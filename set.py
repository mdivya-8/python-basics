
a={10,20,}
print(a)
print(type(a))
print(tuple(a))
print(list(a))
b=a.add(30)
print(b)
#difference
a={1,2,3,4,5}
b={1,2,3}
a.difference(b)
print(a)
b.difference(a)
dir(a)
print(b)
dir(a)
#all(),#any()
d={1,2,3,4,5}   #all()
e=all(d)
f=any(d)
print(e)
print(f)

f={0,1,2,3,4,5}   #any()
g=all(f)
h=any(f)
print(g)
print(h)

h={0,0,0,1}
print(all(h))
print(any(h))

s={"mango","tree"}
"mango" in s    
print(s)         #true
"divya" not in s  
print(s)          #true
st={"mango","tree",(1,2,3)}
f={0,1,2,3,4,5}
print(st)
print(st | f)    # or |
print(st & s)     # and &
print(st - f)      # -
s1={"mango","tree"}
s1.add("div")    #add()
print(s1)
s1.pop()         #pop()
print(s1)
name={"div","divya"}
name1={"tree"}
name.copy()   #copy()
print(name)
#my1=name1.remove("div")     #remove()
#print(my1)
st1={10,20,30,"mango","tree",(1,2,3)}      #len()
print(len(st1))
c1={10,20,30,40,60,70}
#max(c1)
print(max(c1))  #max()
print(min(c1))   #min()
print(len(c1))   #len()
print(sum(c1))   #sum()

#a=input("enter a elementn")
#b=input("enter b element")
#print(int(a+b))
#print(int(a)+int(b))
