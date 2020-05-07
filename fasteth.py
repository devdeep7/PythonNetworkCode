import re

broadlist = []
with open("intstat", "rt") as intfile:
	for i in intfile:
		y=re.search(r"broadcasts",i)
		w=re.search(r"FastEthernet",i)
		if w!=None:
			print (i)
		elif y!=None:
			z = re.search(r"[0-9]+", i)
			print (z.group())
			print (i)
			broadlist.append(z.group())

print (broadlist)
