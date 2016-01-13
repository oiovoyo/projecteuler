'''



The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?


'''

import sys
import os
sys.path.append(os.path.dirname(sys.argv[0]) + "\\..\\common\\")
import number
N = number.number()





def is_cycle_prime(num):
	#print("%s %s" % (base, num))
	rotate_num = num
	n = len(str(num))
	while True:
		#print("%d %d" % (num, rotate_num))
		if N.is_prime(rotate_num) == False:
			return False
		rotate_num = int (rotate_num / 10) + (rotate_num % 10)*int(N.power(10,n - 1))
		if num == rotate_num:
			break
	return True
def is_number_ok(num):
	check="024685"
	sum = 0
	if num == 2 or num == 5:
		return True
	for i in check:
		#sum  = sum + int(i)
		if str(num).find(i) != -1:
			return False
	return True
def get_result():
	result = 0
	for i in range(2,1000000):
		if is_number_ok(i) and is_cycle_prime(i):
			result = result + 1
			print(i)
	return str(result)
if __name__ == "__main__":
	print ("result is : %s" % get_result())