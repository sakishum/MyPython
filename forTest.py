D = {'a':1, 'b':2, 'c':3}
Ks = list(D.keys())
print(Ks)
Ks.sort()
print(Ks)

for key in Ks:
	print(key, '=>', D[key])

for c in 'Spam':
	print(c.upper())

x = 4
while x > 0:
	print('spam!' * x)
	x -= 1
