def multiply(x,y):
	
	if y<0:
		return -multiply(x,-y)

	result = [0]

	def helper(i):
		if i > y:
			return
		else:
			result[0] = result[0] + x
		helper(i+1)
	
	helper(1)
	return result[0]


print multiply(-3,-400)