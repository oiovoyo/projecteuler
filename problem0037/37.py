'''



The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.


'''

import sys
import os
sys.path.append(os.path.dirname(sys.argv[0]) + "\\..\\common\\")
import number
N = number.number()

def is_truncate_left_prime(num):
	while num > 0:
		if N.is_prime(num) == False:
			return False
		n = len(str(num))
		num = num - int(str(num)[0]) * int(N.power(10, n - 1))
		#print(num)
	return True
def is_truncate_right_prime(num):
	while num > 0:
		if N.is_prime(num) == False:
			return False
		num = int(num / 10)
		#print(num)
	return True
def is_number_ok(num):
	check="0468"
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
	count = 0
	i = 11
	while True:
		if count >= 11:
			break
		if is_number_ok(i) and is_truncate_left_prime(i) and is_truncate_right_prime(i):
			result = result + i
			count = count + 1
			print(i)
		i = i + 1
		#if i % 5000 == 0:
		#	print("now is %d" % i)
	return str(result)
if __name__ == "__main__":
	print ("result is : %s" % get_result())