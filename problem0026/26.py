'''


A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

    1/2	= 	0.5
    1/3	= 	0.(3)
    1/4	= 	0.25
    1/5	= 	0.2
    1/6	= 	0.1(6)
    1/7	= 	0.(142857)
    1/8	= 	0.125
    1/9	= 	0.(1)
    1/10	= 	0.1 

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

analyze:
1/7:
int(10/7)=1
int((10 - 7)*10/7)=4
...

'''
import sys
import os
sys.path.append(os.path.dirname(sys.argv[0]) + "\\..\\common\\")
import number
N = number.number()
def get_result():
	max = 0
	lasti = 0
	for i in range(1,1001):
		n = N.recurring_number_divide_by_1(i)
		if n > max:
			max=n
			lasti = i
	return str(lasti)
if __name__ == "__main__":
	print ("result is : %s" % get_result())