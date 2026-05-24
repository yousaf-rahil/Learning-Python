x = 10
def change():
    x = 5
    print(f"This is the local x: {x} ")

def gchange():
    global x
    x = 99
    print(f"This is the new global x: {x}")

print(f"This is the global x: {x}")
change()
gchange()
print(x)