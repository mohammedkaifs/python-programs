class Employee:
    company= "google"
    salary =100

harry = Employee()
kaif = Employee()

print(harry.company)
print(kaif.company)

# creating instance salary for both the object


harry.salary = 300
# kaif.salary = 500

Employee.company = "youtube"
print(harry.company)
print(kaif.company)
print(harry.salary)
print(kaif.salary)

# below line throws an error because addrss is not present in isinstance class
print(Employee.address)