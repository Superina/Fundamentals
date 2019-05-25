astr = '''
g fmnc wms bgblr rpylqjyrc gr zw fylb. 
rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw 
fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr
 gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. 
lmu ynnjw ml rfc spj.

'''


def rotate(string,num):
	return string[num:] + string[:num]


def letterMap(num):
	alphabet = 'abcdefghijklmnopqrstuvwxyz'
	dict1 = {letter:num for num,letter in enumerate(alphabet)}
	dict2 = {letter:num for num,letter in enumerate(rotate(alphabet,num))}
	map_dict = dict(zip(dict1,dict2))
	return map_dict


def decode(string,map_dict):
	string_list = list(string)
	result = []
	
	for letter in string_list:
		if letter in map_dict:
			result.append(map_dict[letter])
		else:
			result.append(letter)
	return ''.join(result)


# if __name__ == '__main__':
# 	map_dict = letterMap(2)
# 	translation = decode(astr,map_dict)
# 	print(translation)







# # METHOD 2


# def encode(str,num):
# 	return str[num:] + str[:num]

# from string import maketrans

# intab = 'abcdefghijklmnopqrstuvwxyz'
# outtab = encode(intab,2)

# transtab = maketrans(intab,outtab)

# print(astr.translate(transtab))

