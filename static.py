class Employee:
    company = "Google"
    def getsalary(self,signature):
        print(f"salary for this employee working {self.company} is {self.salary}\n{signature}")

    @staticmethod
    def greet():
        print("good morning sir")

    @staticmethod
    def time():
        print("the time is 10am morning")




harry = Employee()
harry.salary = 100000
harry.getsalary("Thanks!")
harry.greet()
harry.time()
