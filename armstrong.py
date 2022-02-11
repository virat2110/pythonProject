import math
n= int(input("enter n value : "))
t = n
c=math.floor(math.log10(n)) + 1
sum=0
arm=0
while n!=0:
    sum = sum+ n%10
    arm = arm + math.pow(n%10, 3)
    n=n//10
if t == arm:
    print(f"{t} is armstrong number with sum: {arm}")
else:
    print("not armstrong number")

print(sum)
print(arm)



