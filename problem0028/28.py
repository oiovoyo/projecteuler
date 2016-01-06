'''


Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?


'''

def get_matrix_diagonals_sum(n):
	n2 = n * n
	add = 2
	addtimes = 0
	sum = 0
	i = 1
	while i <= n2:
		sum = sum + i
		i = i + add
		addtimes = addtimes + 1
		if addtimes == 4:
			addtimes = 0
			add = add + 2
	return str(sum)		

def get_result():
	return get_matrix_diagonals_sum(1001)
if __name__ == "__main__":
	print ("result is : %s" % get_result())