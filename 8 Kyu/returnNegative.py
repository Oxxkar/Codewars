# marzo 12, 2019 
def make_negative(number):
		return -abs(number)


def make_negative(number):
	if number == 0:
		return 0
	elif number < 0:
		return number
	else:
		return int("-" + str(number))
