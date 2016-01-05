'''


A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210
What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
 analyze:
  6789 1   1!
  6798 2   2!
  6879 3   2!+ 1!
  6897 4   2!+ 2!
  6978 5   2!+ 2! + 1!
  6987 6   3!
  7689 7   3!+ 1!
  7698 8   3!+ 2!
  7869 9   3!+ 2!+ 1!
  7896 10  3!+ 2!+ 2! 
  7968 11  3!+ 2!+ 2! + 1! 
  7986 12  3! + 2!+ 2! + 2! 
  8679 13  3! + 3! + 1!
  8697 14  3! + 3! + 2!
  8769 15  3! + 3!+ 2!+ 1!
  8796 16  3! + 3!+ 2!+ 2!
  8967 17  3! + 3!+ 2!+ 2!+ 1!
  8976 18  3! + 3!+ 2!+ 2! + 2! 
  9678 19  3! + 3!+ 3!+ 1!
  9687 20  3! + 3!+ 3!+ 2!
  9768 21  3! + 3!+ 3!+ 2!+ 1!
  9786 22  3! + 3!+ 3!+ 2!+ 2!
  9867 23  3! + 3!+ 3!+ 2!+ 2!+ 1!
  9876 24  3! + 3!+ 3!+ 3!
 
 
  
  the last 3 numbers' order is 3!=6
  N! <= 1,000,000 < (N+1)!
  1,000,000 = a1! + a2! + ... + an!
  if num == N!:
	first N letter reserve order
  a1 * (N - 1) ! + a2 * (N - 2)! + ... + aN-1*1!
  
'''
import sys
import os
sys.path.append(os.path.dirname(sys.argv[0]) + "\\..\\common\\")
import number
N = number.number()

def get_factorial_count(num,n):
	count = 0
	f_n = N.factorial(n)
	count = int(num / f_n)
	if num - count * f_n <= 0:
		count = count - 1
	print("num is %d n is %d count is %d left is %d" % (num,n,count,num - (f_n * count)))
	return {"count":count, "left":num - (f_n * count)}

def pickup_n(string, n):
	print("string is %s n is %d" % (string,n) )
	left = string[0:n]
	if len(string) > n:
		left = left + string[n+1:]
	return {"n":string[n],"left":left}
	
def get_result_num(string, num, n):
	if len(string) == 1:
		return string
	ret = get_factorial_count(num,n)
	result = pickup_n(string,ret["count"])
	return result["n"] + get_result_num(result["left"], ret["left"] , n - 1)

def get_result():
	return get_result_num("0123456789", 1000000, 9)
if __name__ == "__main__":
	print ("result is : %s" % get_result())


