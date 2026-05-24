class employee:
    def __init__(self, n, i):
        self.name = n
        self.id = i
    
    def show(self):
        print(f"The employee is {self.name} and his/her id is {self.id}")

class coder(employee):
    def __init__(self, n, i, l):
        self.name = n
        self.id = i
        self.language = l
    
    def show_lan(self):
        print(f"{self.name} is a coder of language {self.language} and his id is {self.id}")

e1 = employee("Peter", 11)
e2 = employee("Oggy", 3)
e3 = coder("Yousaf", 331, "Python")
e3.show_lan()
e3.show()
print("\n")
e1.show()
print("\n")
e2.show()