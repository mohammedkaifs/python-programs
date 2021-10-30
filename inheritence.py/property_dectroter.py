class Employee:
    comapany = "Bharat Gas"
    salary = 5600
    salarybouns = 400



    @property
    def totalsalary(self):
        return self.salary + self.salarybouns

    @totalsalary.setter
    def totalsalary(self,val):
        self.salarybouns = val -self.salary

e = Employee()
print(e.totalsalary)
e.totalsalary= 5800
print(e.salary)
print(e.salarybouns)