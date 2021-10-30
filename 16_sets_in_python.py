a = {1,3,4,5}
print(type(a))

print(a)

#Important : this syntax will create an empty dictionary and an empty set
a={}
print(type(a))

# An empty set can be using the below syntax:
b=set()
print(type(b))

# adding values to an empty set
b.add(4)
b.add(5)
b.add((7,8))
# b.add({4:5}) # cannot add lists or dictonary in sets

print(b)

print(len(b)) # prints the length of this set

b.remove(5) # removes 5 from set b
# b.remove(51)  #cannot remove 15 because it is not present in set
print(b)

print(b.pop())
print(b)

