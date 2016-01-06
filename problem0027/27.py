'''



Euler discovered the remarkable quadratic formula:

n2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 412 + 41 + 41 is clearly divisible by 41.

The incredible formula  n2 ? 79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79. The product of the coefficients, ?79 and 1601, is ?126479.

Considering quadratics of the form:

    n2 + an + b, where |a| < 1000 and |b| < 1000

    where |n| is the modulus/absolute value of n
    e.g. |11| = 11 and |?4| = 4

Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.


'''
num_type={}
PRIME=1
NOTPRIME=2

def is_prime(num):
	if num == 1:
		return False
	if num_type.get(num) != None:
		return num_type[num] == PRIME
	for i in range(2, int(num/2)):
		if num % i == 0:
			num_type[num] = NOTPRIME
			return False
	num_type[num] = PRIME
	return True
	
def is_consecutive_prime(num1, num2):
	for i in range(num1+1, num2):
		if is_prime(i):
			return False
	return True
def quadratic_result(a,b,n):
	return n*n + a*n + b
def max_consecutive():
	max=0
	result={}
	for a in range(-1000,1001):
		for b in range(-1000,1001):
			n = 0
			p1 = quadratic_result(a,b,n)
			if p1 > 0 and is_prime(p1):
				while True:
					n = n + 1
					p2 = quadratic_result(a,b,n)
					if p2 > 0 and is_prime(p2):
						p1 = p2
						#print("%d %d" % (p1,p2))
					else:
						break
			if n > max:
				max = n
				result = {"a":a,"b":b,"n":n}
				print(result)
	return result
def get_result():
	r = max_consecutive()
	return str(r["a"] * r["b"])
if __name__ == "__main__":
	print ("result is : %s" % get_result())