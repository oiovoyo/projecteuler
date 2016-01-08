# -*- coding: utf-8 -*-
'''


We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 ¡Á 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.



'''
import sys
import os
sys.path.append(os.path.dirname(sys.argv[0]) + "\\..\\common\\")
import number
N = number.number()

def check_product(c):
	d = N.get_divisors(c)
	d.sort()
	for a in d:
		for b in d:
			if a <= b and a * b == c:
				all_str = str(a)+str(b)+str(c)
				#all_str.sort()
				
				check_str="123456789"
				if len(all_str) != 9:
					continue
				if sorted(all_str) == sorted(check_str):
					print ("%d * %d = %d (%s)" % (a, b ,c, sorted(all_str)))
					return True
	return False


def get_result():
	sum = 0
	sum_array=[]
	for c in range(1,99999):
		if check_product(c) == True:
				sum = sum + c
	
	return str(sum)
if __name__ == "__main__":
	print ("result is : %s" % get_result())

	