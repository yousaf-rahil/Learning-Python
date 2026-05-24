a = int(input("Enter Your age: "))
if(a>18):
    print("You can drive")
else:
    print("You cannot drive")

money = 200
shoe = 150
if(money==shoe):
    print("You can buy the shoes")

elif(money>shoe):
    if(money>200):
        print("Shoes bought and You still have 50$+ left")
    elif(money==200):
         print("Shoes bought and You still have 50$ left")   
    else:
        print("Shoes are bought and there is some money left")     
else:
    print("Cannot buy the shoes")


#           MATCH CASE


Speed = int(input("Enter your speed: "))

match Speed:
    case a if a in range(0,20):
        print("Cycle")
    case b if b in range(21, 50):
        print("Bike")
    case c if c in range(51, 100):
        print("Car")
    case _:
        print("spaceship")


day = input("Enter the day: ").capitalize()
match day:
   case "Monday":
      print("Working day")
   case "Tuesday":
      print("Working day")
   case "Wednesday":
      print("Working day")
   case "Thursday":
      print("Working day")
   case "Friday":
      print("Half-day")     
   case _:
      print("Weekend")    