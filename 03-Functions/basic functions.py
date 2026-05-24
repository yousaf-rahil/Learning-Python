def mean(a,b):
    print((a+b)/2) 
def gmean(a,b):
    print((a*b)/(a+b))

a= int(input("Enter a number: "))
b= int(input("Enter another number: "))

mean(a,b)
gmean(a,b)

def bmean(*numbers): #--> * is used to get a tuple as input 
    sum = 0
    for i in numbers:
        sum = sum + i
    
    return sum/ len(numbers)

print(bmean(2,3,4,6))

