# Initiate a matrix of size m x n.
# The trick here is to use generator. This is the easiest most Pythonic way.


def make_matrix(n,m):
	return [[None] * m for i in range(n)]


print make_matrix(3,4)