
for a in range(0,10):
    print(a)
    if(a == 9):
        print("About to end")
    
Cats = ["Daffy", "Shadow", "Bubble", "Oggy", "Katie", "Bunny", "Snow", "Noody", "Cookie", "Peter", "Ringo", "Ladu", "kene"]
for name in Cats:
    print(name)

for i in range(0, 22, 2):
    print(i)

#           while loop
i = 0
while(i<21):
    print(i)
    i = i+1

#            Break continue
for i in range(0,11):
    print(i)
    if i ==9:
        break

print("Not gonna end")

for j in range(0,12):
    if j ==9:
     print("About to end")
     continue
    print(j)