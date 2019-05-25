def factorial(n):
	result = [None] * (n+1)
	result[0] = result[1] = 1

	def helper(i):
		if i > n:
			return
		else:
			result[i] = i * result[i-1]
		helper(i+1)

	helper(2)
	return result[n]




print factorial(4)