import time

def forloop():
    for i in range(100):
        print(i)

init = time.time()

forloop()
print(time.time()-init)

name = input("Enter Your Name: ")
time.sleep(4)
print(f"Hello {name}!! Welcome to the python")

t = time.localtime()
format_t = time.strftime("%Y %m %d , %H:%M:%S")
print(t)

print(format_t)