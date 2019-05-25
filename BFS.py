'''
Write a BFS of my own to understand how to traverse through tree/graph like structure

    B - D
  / |  /| \
A   | / |  F
  \ |/  |  
    C - E

'''


graph = {
	'A':['B','C'],
	'B':['A','C','D'],
	'C':['A','B','D','E'],
	'D':['B','C','E','F'],
	'E':['C','D'],
	'F':['D']


}

def BFS(graph,start):
	queue = []
	queue.append(start)
	seen = set()
	seen.add(start)
	parent = {start:None}
	
	while len(queue) > 0:
		vertex = queue.pop(0)
		nodes = graph[vertex]
		for n in nodes:
			if n not in seen:
				queue.append(n)
				seen.add(n)
				parent[n] = vertex 
		# print(vertex)
	return parent


parent = BFS(graph,'E')
print(parent)
# BFS(graph,'E')

'''

To get the shortest distance from starting point E to B

Backtrack from B, what's the point prior to B?
'''

v = 'B'

while v != None:
	print(v)
	v = parent[v]





