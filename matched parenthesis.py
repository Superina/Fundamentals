str1 = '[]()()(((([])))'
str2 = '(())}'
         

def is_matched(expression):

	opening = ['[','(','{']
	closing = [']',')','}']
	mapping = dict(zip(opening,closing))
	queue = []

	for letter in expression:
		if letter in opening:
			queue.append(mapping[letter])
		elif letter in closing:
			if not queue or letter != queue.pop():
				return False
		else:
			return False
	return not queue



# print is_matched(str1)
print is_matched(str2)