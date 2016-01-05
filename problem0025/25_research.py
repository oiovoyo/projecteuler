'''


The Fibonacci sequence is defined by the recurrence relation:

    Fn = Fn-1 + Fn-2, where F1 = 1 and F2 = 1.

Hence the first 12 terms will be:

    F1 = 1
    F2 = 1
    F3 = 2
    F4 = 3
    F5 = 5
    F6 = 8
    F7 = 13
    F8 = 21
    F9 = 34
    F10 = 55
    F11 = 89
    F12 = 144

The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?


analyze:



'''
import sys

def get_10_power(num):
	count = 0
	while int(num / 10) > 0:
		count = count + 1
		num = int(num / 10)
	return count
def get_digit_count(num):
	return len(str(num))
def get_result():
	fn = 1
	fn1 = 1
	fn2 = fn + fn1
	lasti = 0
	lastii = 0
	i = 3
		
	for i in range(3,2000000):
		fn2 = fn + fn1
		nfn = fn1
		nfn1 = fn2
		if get_digit_count(fn2) == int(sys.argv[1]):
			print("%d:%d\n" % (i,fn2))
			return i
		
		'''
		if get_10_power(fn2) != get_10_power(fn1):
			if (i - lasti) == 4:
				if (i - lastii) == 19:
					print("%d\n" % (i))
				lastii = i
			lasti = i
			#print("%d:%d\n" % (i,fn2))
		'''
		fn = nfn
		fn1 = nfn1
	return "1"
if __name__ == "__main__":
	print ("result is : %s" % get_result())