class person:
    country = 'India'
    def takeBreath(self):
        print("I am breathing")


class Employee(person):
    company = "honda"


    def getSalary(self):
        print(f"Salary is {self.salary}")


    def takeBreath(self):
        super().takeBreath()  
        print("I am an Employee so i am luckily breathing")


class programmer(Employee):
        company = "fiverr"

        def getsalary(self):
            print ("Np salary to programmer")

        def takeBreath(self):
            super().takeBreath()
            print("I am an Employee so i am luckily breathing++++")





p = person()
p.takeBreath()

e  =Employee()
e.takeBreath()

pr = programmer()
pr.takeBreath()
