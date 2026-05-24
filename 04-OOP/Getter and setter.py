class new_class:

    def __init__(self, value):
        self._value = value
    
    @property
    def ten(self):
        return 10 *self._value 
    
    @ten.setter
    def ten(self, new_val):
        self._value = new_val 
    
    def show(self):
        print(f"This is the value: {self._value}")
    
obj = new_class(67)

print(f"The value before using the getter and setter is: {obj._value}\n"), 

obj.ten = 50
print(f"The value from getter is: {obj.ten}")
print(f"The value of thr variable is: {obj._value}")

obj.show()