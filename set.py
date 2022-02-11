def intersection(a,b,c):
    t = (set(a).intersection(set(b)))
    print(t.intersection(set(c)))

def union(a,b,c):
    t = (set(a).union(set(b)))
    print(t.union(set(c)))

def subtract(a,b,c):
    t = (set(a).difference(set(b)))
    print(t.difference(set(c)))

a=[10,20,30,60,70]
b=[30,40,50,20]
c=[20,30,60,10]
intersection(a,b,c)
union(a,b,c)
subtract(a,b,c)