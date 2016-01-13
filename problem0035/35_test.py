import math  
def isPrime(n):  
	for i in range(2,int(math.sqrt(n))+1):  
		if n%i==0:  
			return False  
	return True  
def isCyclePrime(n):  
	num = list()
	orgn=n
	while n > 0:  
		num.insert(0,n%10)  
		n /= 10  
	for i in range(len(num)):  
		s = ''  
		for k in range(i,len(num)):  
			s += str(num[k])  
		for j in range(i):  
			s+=str(num[j])  
		if isPrime(int(s)) == False:  
			return False  
	print(orgn)
	return True  
def main():  
	count =0  
	for i in range(2,1000000):  
		if isCyclePrime(i):  
			count += 1  
	print count  
if __name__ == "__main__":  
	main()  