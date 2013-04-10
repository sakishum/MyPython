# you can use str(a) which gives you a string object of int(2)
file = open("sample.log")
sum = 0
while 1:
	line = file.readline()
	if not line:
		break
	print(line)
	sum += int(line)
	pass
print("Sum : " + str(sum))
