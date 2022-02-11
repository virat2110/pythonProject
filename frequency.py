a = []
b = []
size = int(input("Enter number of elements : "))

for i in range(0, size):
    d = int(input())
    a.append(d)

for i in range(0,size):
    if a.count(a[i])>1:
        b.append(a[i])
print(b)




