a= [3,6,9,2,4,23,343,45,44,66]
# b=[]
# for item in a:
#     if item%2==0:
#         b.append(item)


# print(b)

b= [i for i in a if i%2==0]
print(b)


# set comperihenison
t = [1,2,3,4,1,4,3]
s= {i for i in t}
print(s)
