'''
common class for number
'''
def array_find(arr, item):
	for i in arr:
		if i == item:
			return True
	return False
class number:
	def __init__(self):
		return
	def get_divisors(self, num):
		divisors=[]
		for i in range(1, int(num/2) + 1):
			if num % i == 0:
				divisors.append(i)
		return divisors
	def factorial(self, n):
		if n <= 1:
			return 1
		return n * self.factorial(n - 1)
	
	def number_divide(self, num, divide):
		d = int (num / divide)
		m = int (num % divide)
		return {"div":d,"mod":m}
	def get_min_integer(self,num):
		i = 1
		while int(i/num) == 0:
			i = i * 10
		return i

	def recurring_number(self,num):
		d = self.get_min_integer(num)
		
		dm = self.number_divide(d,num)
		dm_array = []
		#print(dm)
		while array_find(dm_array, dm) == False:
			#result = result * 10 + dm["div"]
			dm_array.append(dm)
			dm = self.number_divide(dm["mod"]*10,num)
			
			#print(result)
			#print(dm)
		result = 0
		begin = False
		for i in dm_array:
			if i == dm:
				begin = True
			if begin == True:
				result = result * 10 + i["div"]
		return result
	def recurring_number_divide_by_1(self,num):
		'''
		1/3	= 	0.(3)
		recurring_number_divide_by_1(3) == 3
		1/6	= 	0.1(6)
		recurring_number_divide_by_1(6) == 6
		1/7	= 	0.(142857)
		recurring_number_divide_by_1(7) == 142857
		'''
		return self.recurring_number(num)