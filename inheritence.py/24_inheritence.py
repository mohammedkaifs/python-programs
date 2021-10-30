
# single inheritence example also


class Employee:
    comapny = "google"


    def showDetails(self):
        print("This is an employee")


class programmer(Employee):
    language = 'python'



    def getlanguage(self):
        print(f"The language is {self.language}")


    def showDetails(self):
        print("This is an programmer")


e = Employee()
e.showDetails()
p = programmer()
p.showDetails()
# print(p.comapny)