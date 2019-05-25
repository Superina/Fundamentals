# path_list = ['/home/anti-depressants/xanax',
# 			 '/home/heart/lipitor',
# 			 '/home/heart/atorvastatin',
# 			 '/home/heart/lipitor',
# 			 '/home/heart/heart',
# 			 '/drugs/nasal/flonase',
# 			 '/drugs/topical',
# 			 '/drugs/routes/oral/tablets',
# 			 '/drugs/routes/nasal/flonase']


path_list = ['/home/anti/xanax',
             '/home/heart/lipitor',
             '/home/heart/atova']

# path_list = ['/home/anti/xanax']

new_list = []
adict = {}

for path in path_list:
	new_list.append(path.split('/'))

# print ('I am the new list: {}'.format(new_list))

for minilist in new_list:
	current = adict
	for folder in minilist:
		if folder not in current:
			current[folder] = {}
		current = current[folder]


import pprint
pp = pprint.PrettyPrinter(indent=2)
pp.pprint(adict)

















# The following code is to understand how the value of current changed while looping

# for minilist in new_list:
# 	current = adict
# 	for folder in minilist:
# 		if folder not in current:
# 			current[folder] = {}
# 			pp.pprint('this is current before {}'.format(current))
# 		current = current[folder]
# 		pp.pprint('this is current after {}'.format(current))
