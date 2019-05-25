alist = [[1,2,3],[4,5,6],[7,8,9]]

flat_list = [ item for sublist in alist for item in sublist]

print(flat_list)