'''
common class for number
'''
import math
def array_find(arr, item):
	for i in arr:
		if i == item:
			return True
	return False
num_type={}
PRIME=1
NOTPRIME=2
class number:
	def __init__(self):
		return
	def is_prime(self, num):
		'''
		>>> a = number()
		>>> a.is_prime(23)
		True
		>>> a.is_prime(21)
		False
		'''
		if num == 1:
			return False
		if num_type.get(num) != None:
			return num_type[num] == PRIME
		for i in range(2, int(num/2) + 1):
			if num % i == 0:
				num_type[num] = NOTPRIME
				return False
		num_type[num] = PRIME
		return True
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
	def power(self, n, a):
		return math.pow(n,a)
	def sqrt(self, n):
		return math.sqrt(n)
	def simple_factor(self, a, b):
		s_a = self.get_divisors(a)
		r_a = a
		r_b = b
		for i in s_a:
			if r_b % i == 0:
				r_a = r_a / i
				r_b = r_b / i
				
		return {'n':r_a,'d':r_b}
	def change_to_base(self, num, base):
		'''
		>>> a = number()
		>>> a.change_to_base(2,2)
		'10'
		>>> a.change_to_base(3,2)
		'11'
		>>> a.change_to_base(4,2)
		'100'
		>>> a.change_to_base(9,9)
		'10'
		>>> a.change_to_base(10,9)
		'11'
		>>> a.change_to_base(17,9)
		'18'
		'''
		if base >= 10:
			return str(num)
		ret = ""
		while num != 0:
			mod = str(num % base)
			ret = mod + ret
			num = int (num / base)
		return ret
	def is_palindromic(self, num, base):
		'''
		>>> a = number()
		>>> a.is_palindromic(3,2)
		True
		>>> a.is_palindromic(4,2)
		True
		>>> a.is_palindromic(5,2)
		True
		'''
		str_num=str(num)
		if base != 10:
			str_num = self.change_to_base(num, base)
		list_num = list(str_num)
		#while list_num[len(list_num) - 1] == "0":
		#	list_num = list_num[0:len(list_num) - 1]
		list_len = len(list_num) 
		for i in range(0, int (list_len / 2)):
			if list_num[i] != list_num[list_len - i - 1]:
				return False
		return True
if __name__ == "__main__":
	import doctest
	doctest.testmod()