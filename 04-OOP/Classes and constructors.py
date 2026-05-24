class car:
    # model = "Civic"
    # make = "2020"
    # company = "Honda"
    
    def __init__(self, mo, ma, co):  #----> Constructor
        self.model = mo
        self.make = ma
        self.company = co

    
    def info(self):
        print(f"The car is {self.model} of {self.make} and company {self.company}")

a = car("Civic", "2020", "Honda")

b = car("Corrola", "2023", "Toyota")

a.info()
b.info()
a.model = "Carrola"
a.company = "Toyota"
a.info()
b.info()