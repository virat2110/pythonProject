s=[30189,"virat",70,80,90,100,98]
print(s)

print(s[0])
print(s[0:2])
print(s[2:])
print(s[:3])
print(s[:])
print(s[-1])
print(s[-1:-7])  # lower bond always less than upeer bond   so gives empty array
print(s[-7:-1])
print(s[-1:-7:-1])  # gives data in reverse order
print(s[::-1])    # returns total string in reverse order
print(s[::-2])    # skip every second element in an reverse order
print(s[0:7:2])

print('for loop')
for i in range(1,10):
    print(i)
for i in range(5,1):   # not return anything
    print(i)

for j in range(5,-1,-1):
    print(j)

L=[i for i in range(10)]   # return list from 0 to9
print(L)


p=[i**2 for i in range(10)]   # Squares of numbers  from 0to 9
print(p)

a=[1,2,3,4]
del a[3]
b=[4,5,6]
print(a+b)
print(a*2)

print(7 in a)  # used to check if avialable or not

c=a   # assigning a list to c
c[0]=5  # change for both a and c
print(c)
print(a)

a.append([4, 5, 6])    # append as another list
print(a)
a.extend([9, 10, 11])   # append as a single list
print(a)
a = [[1, 2], [3, 4], [5, 6]]
print(a[1])
print(a[2][1])
for i in a[2]:
    print(i)

print('list comprehension')
square = [x**2 for x in range(1, 11)]
print(square)

print("tuple")
print("it cannot be modified it is immutable")
t = (10, "virat", 20, 30, 40)
print(t)
print(t[1])
print(t[-1])
print(len(t))  # length of tuple
print(" lenth of tuple be method len", len(t))
s = (("virat", 10, 20), ("ankit", 30, 40), ("achyuta", 50, 60))
print(s[2][0])

print("set...to maintain unique vlaues")
s = set("apple")
print(s)
print(s)

print("dictionary   key,value")

d={'regd': 31089, 'name': 'aishik', 'dob': 2001}
print(d['regd'])
print("dictionary is mutable but keys are immutable and keys are unique")
print("changing value with respect to key")
d['name'] = 'virat'
print(d)
print(d.get('regd'))
print(d.keys())  # returns as list
print(d.values())    # returns as list

d = {"a": {'c':  123, 'd': [1, 2, 3, 4, 5]}, 'b': [5, 6, 7, 8]}
print(d['a']['d'])



print("function defination")
def display(u):
    print(u)
display(10)




 











