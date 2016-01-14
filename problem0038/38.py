# -*- coding: utf-8 -*-
'''


Take the number 192 and multiply it by each of 1, 2, and 3:

    192 × 1 = 192
    192 × 2 = 384
    192 × 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?


'''

import sys
import os
sys.path.append(os.path.dirname(sys.argv[0]) + "\\..\\common\\")
import number
N = number.number()

def is_pandigital(num):
	n = 1
	str_pandigital=""
	while len(str_pandigital) < 9:
		str_pandigital = str_pandigital + str(num * n)
		n = n + 1
	if sorted(str_pandigital) == ['1','2','3','4','5','6','7','8','9']:
		return int(str_pandigital)
	return 0
def get_result():
	result = 0
	i = int(123456788 / 2)
	
	while True:
		#print(i)
		p = is_pandigital(i)
		if p > result:
			print("%d %d" % (result,p))
			result = p
				
		i = i - 1
		if i == 0: 
			break
	return str(result)
if __name__ == "__main__":
	print ("result is : %s" % get_result())