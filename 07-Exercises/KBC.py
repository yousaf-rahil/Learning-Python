#------------>Exercise 3 (KBC)
questions = ["What is the capital of Pakistan?",  "Who is the current presedent of US?", "Is Python easy?"]
answers = ["Islamabad", "Donal duck", "Yes"]

print(questions[0])
ans = input("Enter your answer: ").capitalize()
cash =0
if ans == answers[0]:
    print("Correct answer!!")
    cash = cash+100
else:
    print("Wrong answer!")

print(questions[1])
ans1 = input("Enter your answer: ").capitalize()

if ans1 == answers[1]:
    print("Correct answer!!")
    cash = cash+100
else:
    print("Wrong answer!")    

print(questions[2])
ans2 = input("Enter your answer: ").capitalize()
if ans2 == answers[2]:
    print("Correct answer!!")
    cash = cash+100
else:
    print("Wrong answer!")

print("Your total prize is: ", cash, "$")


# print("Is Yousaf Raheel Hot??")
# answer= input().strip().capitalize()
# if answer == "Yes":
#     print("Awww Thank you!!!")
# else:
#     print("Wrong ans")
