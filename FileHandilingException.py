try:
    file = open("t1.txt","r")
    try:
        file.write("Hi! i am Virat Anand")
        print("written successfully")
    except IOError as e:
        print(e)
    try:
        a = file.readline()
        print("read successfully")
        print(a)
    except IOError as e:
        print(e)
    finally:
        file.close()
except IOError as e:
    print(e)
