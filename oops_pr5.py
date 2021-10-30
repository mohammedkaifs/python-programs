class train:
    def __init__(self,name,fare,seats):

        self.name=name
        self.fare = fare
        self.seats= seats

    def getstatus(self):
        print(f"The name of train {self.name}")
        print(f"The seats available in train {self.seats}")

    def fareinfo(self):
        print(f"The price of the ticket is :Rs{self.fare}")

    def bookticket(self):
        if(self.seats>0):
            print(f"your ticket has been booked! your seat number is {self.seats}")
            self.seats = self.seats-1
        else:
            print("sorry this train is full kindly try in tatakal")

        def cancelticket(self,seatno):
            pass

intercity = train("intercity express: 14015",90,300)
intercity.getstatus()
intercity.bookticket()
intercity.bookticket()
intercity.getstatus()