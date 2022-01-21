try:
    a = int(input("enter a"))
    b = int(input("enter b"))
    c=a/b
    print("a/b = %d"%c)
except Exception as e:
    print("cannot divide by zero")

else:
    print("in else block")
finally:
    print("finally will always run")






