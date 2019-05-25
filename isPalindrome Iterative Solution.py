#        01234567
word1 = 'abcdecba'
word2 = 'abcdcba'


# n = len(word1)

# for i in range(n):
# 	print(i,n-1-i)

def isPalindrome(word):
	length = len(word)

	for i in range(int(length/2)):
		if word[i] != word[length-1-i]:
			return False
	return True



# print(isPalindrome(word1))
# print(isPalindrome(word2))

