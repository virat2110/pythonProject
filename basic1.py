def printinfo(name,age):
    print("output for fxn printinfo is: ")
    print("name: ",name)
    print("age: ",age)
printinfo("virat",20)

def display(arg1, *vartuple):
    print("output for fxn display is: ")
    print(arg1)
    for var in vartuple:
        print(var, end=' ')
display(10)
display(100,20,30,40,50)
display(10000,200000,30000)     # first value is going in arg1

print()
def digsum(n):
    s=0
    while(n>0):
        d=n%10
        s=s+d
        n=n//10
    return s

print(digsum(12345))

 



