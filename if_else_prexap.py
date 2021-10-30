# names = ["kaif","darsh","aman","swaraj"]
# name = input("Enter the name\n")

# if name in names:
#    print("your name is present in the list")
# else:
#      print("your name is not present in the list")






# 2nd program

marks = int(input("Enter the marks\n"))

if marks>=90:
   grade = "Distinction"
elif marks>=80:
   grade = "A"
elif marks>=70:
   grade = "B"
elif marks>=60:
   grade = "C"
elif marks>=50:
   grade = "D"
else:
   grade = "Fail"

print("your grade is "+ grade)