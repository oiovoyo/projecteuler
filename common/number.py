'''
common class for number
'''

class number:
	def __init__(self):
		return
	def get_divisors(self, num):
		divisors=[]
		for i in range(1, int(num/2) + 1):
			if num % i == 0:
				divisors.append(i)
		return divisors
	