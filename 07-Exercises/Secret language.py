def encode():
    value = input("Enter your word: ").strip().capitalize()
    value1 = value.replace(" ","")
    if len(value1) <=3:
        print(f"{value1[1:].lower()}{value1[0].lower()}")
    else:
        print(f"gtg{value1[1:].lower()}{value1[0].lower()}tex")

def decode():
    value = input("Enter your word: ").strip().capitalize()
    value1 = value.replace(" ", "")
    if len(value1) <=3:
        print(f"{value1[-1].lower()}{value1[:-1].lower()}")
    else:
        print(f"{value1[-4].lower()}{value1[3:-4].lower()}")


option = input("Do you want to encode or decode: ").strip().lower()
if option == "encode":
    encode()
elif option == "decode":
    decode()
else:
    print("Pick the right option")