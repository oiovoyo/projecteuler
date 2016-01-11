'''




145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.



'''
import sys
import os
sys.path.append(os.path.dirname(sys.argv[0]) + "\\..\\common\\")
import number
N = number.number()

def research():
	i = 9
	count  = 1
	while i <= count * N.factorial(9):
		print("%d" % (i))
		i = i * 10 + 9
		count = count + 1
def get_factorial_sum(num):
	sum = 0
	for i in sorted(str(num)):
		sum = sum + N.factorial(int(i))
	return sum
def get_result():
	result = 0
	for i in range(3,999999):
		if get_factorial_sum(i) == i:
			result = result + i
	return str(result)
if __name__ == "__main__":
	print ("result is : %s" % get_result())