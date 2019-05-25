'''
You have 

three $20 dollar bills, 
five $10 dollar bills, 
two $5 dollar bills, 
and five $1 dollar bills. 

How many ways can you make change for a $100 dollar bill?
'''
import pprint
import itertools as it
pp = pprint.PrettyPrinter(indent=4)

bills = [20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]



def breakChange(bills,toAmount):
	num_of_bills = len(bills)
	result = []
	for i in range(num_of_bills):
		group_tup_list = list(it.combinations(bills,i))
		sum_toAmount_list = [tup for tup in group_tup_list if sum(tup) == toAmount]
		for tup in sum_toAmount_list:
			if tup not in result:
				result.append(tup)
	return result




pp.pprint(breakChange(bills,100))







print(list(it.combinations_with_replacement([1, 2], 2)))

print(list(it.permutations(['a', 'b', 'c'])))