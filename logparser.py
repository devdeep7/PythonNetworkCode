
import re
pattern = re.compile(r"http") 
count = 0
lines = 0 
with open("conn.log", "rt") as file:
	line=0
	while (line<400):
		for x in file:
			match = pattern.search(x)
			print(match)
			if match==None:
				break
			else:
				count+=1
			break
		line +=1
		lines = line
print ("Number of times SSL apears in first " + str(lines) + " is " + str(count))
