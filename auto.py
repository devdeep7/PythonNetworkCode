mylines = []
with open ("lorem.txt", "rt") as myfile:
#currentfile = myfile.read()
	for lines in myfile:
		mylines.append(lines)
count = 1
x = 0
index=0
y =0
tobefound="e"
while y <len(mylines):
	substr = mylines[y]
	for i in range (0, len(substr)-1):
		index=substr.find(tobefound, index)
		if index==-1:
			break
		else:
			print ("e", end="")
			count = count+1
			index = index + len(tobefound)
	print('\n' + substr)	
	y=y+1
	index=0
	print (count)
	


#print(mylines[x])
#print (mylines)	
#print(currentfile)
