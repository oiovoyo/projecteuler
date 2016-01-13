'''


The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)



'''

import sys
import os
sys.path.append(os.path.dirname(sys.argv[0]) + "\\..\\common\\")
import number
N = number.number()

def get_result():
	result = 0
	for i in range(1,1000000):
		if N.is_palindromic(i,10) and N.is_palindromic(i,2):
			result = result + i
			print(i)
	return str(result)
if __name__ == "__main__":
	print ("result is : %s" % get_result())