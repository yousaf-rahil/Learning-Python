import time
timestamp = int(time.strftime('%H'))
print(timestamp)

if(timestamp<=9):
    print("Good morning sir")
elif(timestamp>9 and timestamp<=17):
    print("Good afternoon sir")
elif(timestamp>17 and timestamp<=19):
    print("Good evening sir")
else:
    print("Good night sir")