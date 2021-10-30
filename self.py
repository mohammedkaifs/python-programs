class Employee:
    company = "Google"
    def getsalary(self):
        print(f"salary for this employee working {self.company} is {self.salary}")




harry = Employee()
harry.salary = 100000
harry.getsalary()