class math:
    def __init__(self, n):
        self.num = n

    def add_val(self, n):
        return self.num +n


    @staticmethod
    def addval(a,b):
        return a+ b
    

obj = math(10)

print(obj.num)
print(obj.add_val(9))
print(obj.addval(11, 20))