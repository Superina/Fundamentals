'''
Write a DFS of my own to understand how to traverse through tree/graph like structure

    B - D
  / |  /| \
A   | / |  F
  \ |/  |  
    C - E

The only difference btw BFS and DFS is that DFS changed pop(0) into pop(), which pop the last
element in the stack, instead of the 1st element in the queue
'''


graph = {
	'A':['B','C'],
	'B':['A','C','D'],
	'C':['A','B','D','E'],
	'D':['B','C','E','F'],
	'E':['C','D'],
	'F':['D']


}

def DFS(graph,start):
	stack = []
	stack.append(start)
	seen = set()
	seen.add(start)
	
	while len(stack) > 0:
		vertex = stack.pop( )
		nodes = graph[vertex]
		for n in nodes:
			if n not in seen:
				stack.append(n)
				seen.add(n)
		print(vertex)


DFS(graph,'A')
# DFS(graph,'E')