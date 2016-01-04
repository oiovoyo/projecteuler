'''
project euler problem 23 :


A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.


'''

import sys
import os
sys.path.append(os.path.dirname(sys.argv[0]) + "\\..\\common\\")
import number
N = number.number()


	
UNKNOWN_NUMBER=0
PERFECT_NUMBER=1
DEFICIENT_NUMBER=2
ABUNDANT_NUMBER=3


g_number_type={}

def number_type(num):
	global g_number_type
	if g_number_type.get(num) != None:
		return g_number_type[num]
	t=UNKNOWN_NUMBER
	divisors = N.get_divisors(num)
	sum = 0
	for d in divisors:
		sum = sum + d
	if sum < num:
		t = PERFECT_NUMBER
	if sum == num:
		t = DEFICIENT_NUMBER
	if sum > num:
		t = ABUNDANT_NUMBER
	g_number_type[num] = t
	return t

def is_sum_two_abundant_number(num):	
	for i in range(1, int(num/2) + 1):
		if number_type(i) == ABUNDANT_NUMBER and number_type(num - i) == ABUNDANT_NUMBER:
			#print("%d is ok [ %d %d ]" % (num, i, num - i))
			return True
	print("%d is ok" % (num))
	return False
	
MAX_SUM_ABUNDANT = 28123
MIN_SUM_ABUNDANT = 1
def get_result():
	sum=0
	for i in range(MIN_SUM_ABUNDANT,MAX_SUM_ABUNDANT):
		if is_sum_two_abundant_number(i) == False:
			sum = sum + i
	return sum
if __name__ == "__main__":
	print ("result is : %d" % get_result())