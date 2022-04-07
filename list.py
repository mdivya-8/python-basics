#LIST:list is a collection of collection of elements,enclosed by square brackets[].
#mutable:id can change but values are not change.
list=[]
print(list) #empty[]
list1=[1,2,3,4,5]#number[]

print(list1)
list2=[1,2,"string",3,4.5,5]#mixed[]
print(list2)

list3=[1.3,2.5,3.50,4.79,5.78]  #float[]
print(list3)
#print(delete(list3))

list4=[1.3,2.5,[3.50,4.79],5.78] #nested[]
print(list4)
a=[10,20,30,40,"hello",4.5]
print(a)
print(a[2])
print(a[1:])
print(id(a))
print(id(a)-234)
print(len(list))

b=a+["hi","mango"]
print(b)

a.append("mango")
print(a)
a.remove(a[5])
print(a)
a.insert(5,"hi all")
print(a)
a.pop(1)
print(a)
a=[12,34,56,]
a.clear()
print(a)
a=[10,20,30,40,"hello",4.5]
a.index(40)
print(a)
'''v="mango"
print(list(v))'''
