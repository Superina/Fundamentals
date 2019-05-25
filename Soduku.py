import pprint
pp = pprint.PrettyPrinter(indent=2)
board = [[0, 0, 0, 3, 0, 0, 2, 0, 0],
    	 [0, 0, 0, 0, 0, 8, 0, 0, 0],
    	 [0, 7, 8, 0, 6, 0, 3, 4, 0],
    	 [0, 4, 2, 5, 1, 0, 0, 0, 0],
    	 [1, 0, 6, 0, 0, 0, 4, 0, 9],
    	 [0, 0, 0, 0, 8, 6, 1, 5, 0],
    	 [0, 3, 5, 0, 9, 0, 7, 6, 0],
    	 [0, 0, 0, 7, 0, 0, 0, 0, 0],
    	 [0, 0, 9, 0, 0, 5, 0, 0, 0]]


def isFull(board):
	for i in range(0,9):
		for j in range(0,9):
			if board[i][j] == 0:
				return False
	return True


def possibleEntries(board,i,j):

	possibilityArray = {}

	for x in range(1,10):
		possibilityArray[x] = 0

	# check horizontal
	for y in range(0,9):
		if board[i][y] != 0:
			possibilityArray[board[i][y]] = 1

	#check vertical
	for x in range(0,9):
		if board[x][j] != 0:
			possibilityArray[board[x][j]] = 1

	#create logic to nail (k,l) to the upperleft corner of the 3x3 grid where (i,j) falls
	k=0
	l=0
	
	if i>=0 and i <=2:
		k = 0
	elif i>=3 and i<=5:
		k = 3
	else:
		k = 6
	

	if j>=0 and j<=2:
		l = 0
	elif j>=3 and j<=5:
		l = 3
	else:
		l = 6

	for x in range(k,k+3):
		for y in range(l,l+3):
			if board[x][y] != 0:
				possibilityArray[board[x][y]] = 1
	
	# inverse the possibility Array, set the possible entries with the same key/val, and impossible to 0
	for x in range(1,10):
		if possibilityArray[x] == 0:
			possibilityArray[x] = x
		else:
			possibilityArray[x] = 0

	return possibilityArray



def sodukuSolver(board):
	i = 0
	j = 0

	if isFull(board) == True:
		# print("Puzzle Solved") 
		pp.pprint(board)
	
	else:
		for x in range(0,9):
			for y in range(0,9):
				if board[x][y] == 0:
					i = x
					j = y
					break

	# get all possibilities for i,j
	possibilities = possibleEntries(board,i,j)

	# go through all the possibilities and call the function again and again
	for x in range(1,10):
		if possibilities[x] != 0:
			board[i][j] = possibilities[x]
			# print("i,j is ({},{}). And it is filled by {}".format(i,j,possibilities[x]))
			sodukuSolver(board)
	
	board[i][j] = 0

# print(possibleEntries(board,0,1))
sodukuSolver(board)












