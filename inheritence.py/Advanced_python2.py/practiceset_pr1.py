name = input("Enter your name:")
marks =int(input("Enter your marks:"))
phone =int(input("Enter your phone number:"))


# name ="kaif"
# marks ="34"
# phonenumber = '90192102929'

# a="The name of student is {} and his marks are {} and his phone number is {}".format(name,marks,phonenumber)
# a=f"The name of student is {name} and his marks are {marks} and his phone number is {phonenumber}"
# a=f"The name of student is {name} and his marks are {marks} and his phone number is {phonenumber}"
# print(a)
 
template = "The name of student is {} and his marks are {} and his phone number is {}"
output = template.format(name,marks,phone)
print(output)
