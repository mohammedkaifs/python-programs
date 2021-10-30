class Employee:
    company = "visa"
    ecode  = 120

class freelancer:
    company = 'fiver'
    level = 0

    def upgradelevel(self):
        self.level = self.level + 1


class programmer(Employee,freelancer):
    name = "kaif"


p=programmer()
p.upgradelevel()
print(p.company)

