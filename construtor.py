class Employee:
    company = "Google"

    def __init__(self, name, salary,subunit):
        print("Emplpyee is created ")
        self.name = name
        self.salary = salary
        self.subunit = subunit

    def getdetails(self):
        print(f"the name of employee is {self.name}")
        print(f"the salary of employee is {self.salary}")
        print(f"the subunit of employee is {self.subunit}")


    def getsalary(self,signature):
        print(f"salary for this employee working {self.company} is {self.salary}\n{signature}")

    @staticmethod
    def greet():
        print("good morning sir")

    @staticmethod
    def time():
        print("the time is 10am morning")

harry = Employee("Harry",100,"youtube")
harry.getdetails()






