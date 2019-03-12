# marzo 12, 2019 

def get_middle(s):
	if len(s) == 1:
		return s
	elif len(s) == 2:
		return s
	elif len(s) % 2 == 1:
		return s[(len(s) // 2)]
	else:
		return s[(len(s) // 2)-1 : (len(s) // 2)+1]
