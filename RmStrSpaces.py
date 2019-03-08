# marzo 08, 2019 

#def no_space(x):
#	for i in x:
#		if x[i] == "":
#			x.remove(i)
#		return x

def no_space(x):
	removed = x.replace(" ","")
	return removed
