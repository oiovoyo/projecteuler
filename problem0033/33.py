'''


The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

'''
import sys
import os
sys.path.append(os.path.dirname(sys.argv[0]) + "\\..\\common\\")
import number
N = number.number()

def common_terms(a,b):
	return False
def is_curious(a,b):
	s_a = sorted(str(a))
	s_b = sorted(str(b))
	if s_a[0] != '0' and s_a[0] == s_b[0] and s_a[1] != s_b[1]:
		if int(s_a[1]) * b == int(s_b[1]) * a:
			return True
	if s_a[0] != s_b[0] and s_a[1] != '0' and s_a[1] == s_b[1]:
		if int(s_a[0]) * b == int(s_b[0]) * a:
			return True
	return False
def get_simplist(a,b):
	s_a = sorted(str(a))
	s_b = sorted(str(b))
	if s_a[0] != '0' and s_a[0] == s_b[0] and s_a[1] != s_b[1]:
		return {"n":int(s_a[1]),"d":int(s_b[1])}
	if s_a[0] != s_b[0] and s_a[1] != '0' and s_a[1] == s_b[1]:
		return {"n":int(s_a[0]),"d":int(s_b[0])}
	return 0
def get_result():
	result_n = 1
	result_d = 1
	for a in range(10,100):
		for b in range(10,100):
			if a < b and is_curious(a,b) == True:
				print("%d %d" % (a, b))
				nd = get_simplist(a,b)
				result_n = result_n * nd['n']
				result_d = result_d * nd['d']
	result = N.simple_factor(result_n,result_d)
	return str(result["d"])
if __name__ == "__main__":
	print ("result is : %s" % get_result())