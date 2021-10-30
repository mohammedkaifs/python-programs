def increment(num):
    try:
        int(num) + 1
    except:
        raise ValueError("This is not good-harry")

a= increment('df364')
print(a)

