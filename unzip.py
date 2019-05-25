import itertools as it
'''
Given inputs = [1, 2, 3, 4, 5, 6] and n = 2
Write a function to return [(1, 2), (3, 4), (5, 6)]

'''
inputs = [1, 2, 3, 4, 5, 6]
n = 2


def groupby(array,n):
	iters = [iter(array)] * n
	# the above code return something like [[1,2,3,4,5,6],[1,2,3,4,5,6]] but as iterators
	# becuase the 2 iter(array) in [iter(array),iter(array)] are just 2 references pointing to the SAME iterators
	# when calling the below code
	# the 1st iter(array) returns 1, the 2nd iter(array) returns 2 
	# goes back to the 1st iter(array) again, it returns 3, the 2nd iter(array) returns 4 ...etc
	unzip = zip(*iters)
	return list(unzip)

print(groupby(inputs,n))





'''
There is a problem with this function. Once n=4, it will only return
[(1,2,3,4)]
This happens because zip() stops aggregating elements once the shortest iterable passed to it is exhausted.
'''


'''
To fix this, use itertools.zip_longest()
For example
'''


x = [1, 2, 3, 4, 5]
y = ['a', 'b', 'c']
list(zip(x, y))
# [(1, 'a'), (2, 'b'), (3, 'c')]
list(it.zip_longest(x, y))
# [(1, 'a'), (2, 'b'), (3, 'c'), (4, None), (5, None)]



'''
Revised the above groupby function
'''
inputs = [1, 2, 3, 4, 5, 6]
n = 4

def groupby(array,n):
	iters = [iter(array)] * n
	# the above code return something like [[1,2,3,4,5,6],[1,2,3,4,5,6]] but as iterators
	# becuase the 2 iter(array) in [iter(array),iter(array)] are just 2 references pointing to the SAME iterators
	# when calling the below code
	# the 1st iter(array) returns 1, the 2nd iter(array) returns 2 
	# goes back to the 1st iter(array) again, it returns 3, the 2nd iter(array) returns 4 ...etc
	unzip = it.zip_longest(*iters)
	return list(unzip)

print(groupby(inputs,n))





