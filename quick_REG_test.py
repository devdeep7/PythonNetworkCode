import re

pattern = re.compile("\d+\s\s$")

with open("Arp_info.txt", "rt") as parse:
	for line in parse:
		y = pattern.search(line)
		if y==None:
			pass
		else:
			print (y.group())
