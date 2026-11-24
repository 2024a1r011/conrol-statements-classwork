# create an electricity bill class that stores a customers's name and electricity units used. Calculate the bill using these rates : 3 per unit# for the first 100 units , 5 per units for the next 100 units , 
# and 7 per units above 200 . Add a fixed charge of 50 Dsiplay the customer's name , units used and total bill . If the entered units are negative , display an error message

class ElectricityBill:
    def __init__(self,name,units):
        self.name= name
        self.units =units

    def CalculateBill(self):

        if 0<self.units:
            print("Units cannot be negative ")
            return

        if self.units<100:
            bill = 50 + self.units*3
        elif self.units<200:
            bill +=  self.units*5
        elif self.units<300:
            bill += self.units* 7
            