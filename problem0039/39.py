# -*- coding: utf-8 -*-
'''




If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?

'''

import sys
import os
sys.path.append(os.path.dirname(sys.argv[0]) + "\\..\\common\\")
import number
N = number.number()

def int_sqrt(num):
	return N.sqrt(num)

ret_arr = {}
def angle_triangle():

	for i in range(1, 1000):
		for j in range(1,1000):
			if i < j:
				kk = i * i + j * j
				k = int(int_sqrt(kk))
				if k*k == kk:
					print("%d %d %d" % (i,j,k))
					s = i + j + k
					if s < 1000:
						if ret_arr.get(s) == None:
							ret_arr[s] = 0
						ret_arr[s] = ret_arr[s] + 1
			
	return 0
def get_result():
	result = 0
	angle_triangle()
	max_m = 0
	for i in ret_arr:
		if ret_arr[i] > max_m:
			max_m = ret_arr[i]
			result = i
	print (max_m)
	return str(result)
if __name__ == "__main__":
	print ("result is : %s" % get_result())