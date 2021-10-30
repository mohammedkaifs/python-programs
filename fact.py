# n = 4
# product =1
# for i in range(n):
#     product=product * (i+1)
#     print(product)


def factorial_liter(n):
   product = 1
   for i in range(n):
       product = product * (i+1)
       return(product)

print(factorial_liter(5))
print(f)