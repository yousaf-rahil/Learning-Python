def greet(fx):
        def mfx():
            print("You are in the CAR App\n")
            fx()
            print("\n Thanks for using this app")
        return mfx
@greet
def car():
     print("We have Honda, Toyota, Nissan, Mistobishi available")

car()
greet(car)()
