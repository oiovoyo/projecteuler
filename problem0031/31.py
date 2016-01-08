# -*- coding: utf-8 -*-
'''


In England the currency is made up of pound, pound1, and pence, p, and there are eight coins in general circulation:
   1p, 2p, 5p, 10p, 20p, 50p, pound1 (100p) and pound12 (200p).
It is possible to make pound12 in the following way:
    1¡Ápound11 + 1¡Á50p + 2¡Á20p + 1¡Á5p + 1¡Á2p + 3¡Á1p
How many different ways can pound2 be made using any number of coins?

'''

def get_count(num,array_coin):
	array_coin.sort(reverse = True)
	if num == 0:
		return 1
	if len(array_coin) == 0:
		return 0
	max_coin = array_coin[0]
	sum_count = 0
	for i in range(0, int(num/max_coin)+1):
		sum_count = sum_count + get_count(num - max_coin * i, array_coin[1:])
	return sum_count
	
def get_result():
	result = get_count(200,[1,2,5,10,20,50,100,200])
	return str(result)
if __name__ == "__main__":
	print ("result is : %s" % get_result())

	