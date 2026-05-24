f = open("File.txt", 'w')
f.write("This is he first file for file handeling")
f.close()
f = open("File.txt", 'r')
text = f.read()
#print(text)
f.close()
f = open("File.txt", 'a')
f.write("These are the new lines of in this file. Append mode is being used to save the new text instead of over writing the previous one")
f.close()

f= open("File.txt", 'r')
text = f.read()

print(text)

f = open("File.txt", 'a')
data = ["line 1\n", "line 2\n", "line 3\n"]
f.writelines(data)
f.close()
data = ['line 1\n', 'line 2\n', 'line 3\n']
f = open("File.txt", 'a')
f.writelines(data)
with open("File.txt", 'r') as f:
    content = f.readlines()
    print(content)

f = open("File.txt", 'r')
f.seek(9)
print(f.tell(),'\n')

data = f.read()

#print(data)
f.close()

f = open ("File.txt", 'w')
f.write("ENDING the file!!!")
# f.truncate(6)

with open("File.txt", 'r') as f:
    data = f.read()
    print(data)