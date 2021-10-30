# def farh(cel):
#     return (cel*(9/5))+32

# c=0
# f = farh(c)
# print("Farehenite temperature is" + str(f))



# print("hello", end=" ")
# print("hello", end=" ")
# print("hello", end=" ")
# print("hello", end=" ")

def natural_liter(n):
    sum = 1
    for i in range(n):
        sum = sum + (i+1)
        return sum


def natural_recurssive(n):
    if n==1 or n==0:
        return 1
    return n+ natural_recurssive(n-1)

a= natural_recurssive(6)
print(a)
