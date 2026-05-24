
article = """Many
lines
of 
information
"""
print (article)

for i in article:
    print(i)

name = "Daffy"
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])


name = "daffy"
print(name[-4: -2])

print(name.upper())
print(name.lower())
print(name.replace("daffy", "Shadow"))
print(name.capitalize())
print(name.center(50))
print(name.count("f"))

print(name.find("y"))
print(name.isalnum())
print(name.index("y"))
print(name.swapcase())

#           fstring

name = input("What is your name: ")
age = int(input("Enter your age: "))
country = input("Where are you from: ")
print(f"Hi! I am {name}, I am {age} years old and I am from {country}")

