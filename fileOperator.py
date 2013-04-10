f = open('data.txt', 'w')
f.write('Hello\n')
f.write('World\n')
f.close()

f1 = open('data.txt') 
text = f1.read()
print(text)
print(text.split())
f1.close()

data = open('data.txt', 'rb').read()
print(data)
print(data[4:8])


