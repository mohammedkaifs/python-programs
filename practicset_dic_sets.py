# myDict = {
#     "pankha":"fan",
#     "dabba":"box",
#     "vastu":"item"
# }
# print("Options are",myDict.keys)
# a = input("Enter the hindi word\n ")
# # print("The meaning of your word is:",myDict[a])

# # below line will not throw an error
# print("The meaning of your word is:",myDict.get(a))


#2nd program
# num1= int(input("Enter number 1:"))
# num2= int(input("Enter number 2:"))
# num3= int(input("Enter number 3:"))
# num4= int(input("Enter number 4:"))
# num5= int(input("Enter number 5:"))
# num6= int(input("Enter number 6:"))
# num7= int(input("Enter number 7:"))
# num8= int(input("Enter number 8:"))

# s = {num1,num2,num3,num4,num5,num6,num7,num8}
# print(s)


# program3

# s = {18,"18",18.1}
# print(s)

s=set()
s.add(20)
s.add(20.0)
s.add("20")

print(s)                                                         
print(len(s))

#program5
favlang = {}
a = input("Enter your favorite language shubham\n")
b = input("Enter your favorite language kaif\n")
c = input("Enter your favorite language harry\n")
d = input("Enter your favorite language bakraa\n")
favlang['shubham']=a
favlang['kaif']=b
favlang['harry']=c
favlang['bakraa'] =d

print(favlang)