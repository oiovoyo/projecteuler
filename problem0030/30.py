'''


Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

    1634 = 14 + 64 + 34 + 44
    8208 = 84 + 24 + 04 + 84
    9474 = 94 + 44 + 74 + 44

As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.


'''
import sys
import os
sys.path.append(os.path.dirname(sys.argv[0]) + "\\..\\common\\")
import number
N = number.number()

def get_n_digit(num,n):
	str_num=str(num)
	if len(str_num) - 1 < n:
		return 0
	return int(str_num[n])
def get_power_result(num):
	l = len(str(num))
	sum = 0
	for i in range(0,l):
		sum = sum + int(N.power(get_n_digit(num,i), 5))
	return sum
def get_result():
	a=2
	b= int(N.power(9,5)) * 5
	result = 0
	for i in range(a,b+1):
		ret = get_power_result(i)
		if ret == i:
			result = result + ret
	return str(result)
if __name__ == "__main__":
	print ("result is : %s" % get_result())
