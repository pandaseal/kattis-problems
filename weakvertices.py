# For this problem, find weak vertices in 
# graphs – those vertices that is not part of any triangle.
# Descr: https://open.kattis.com/problems/weakvertices

# output:
# one entry per graph: a list of weak vertices

# list of adjacency matrices, one for each graph in the problem
graphs = [] 

# read graphs
n = int(input())
while not (n == -1):
    graph = []
    for i in range(n):
        edges = [int(e) for e in input().split()]
        graph.append(edges)
    graphs.append(graph)
    n = int(input())

weak_vertices = []
for graph in graphs:
    n = len(graph)

    # dict with a list of neighbors for each vertice
    neighbors = {}
    weak = []

    # remap into neighbor list
    for (i, edges) in zip(range(n), graph):
        neighbors[i] = []
        for (j, edge) in zip(range(n), edges):
            if edge == 1:
                neighbors[i].append(j)

    # search for weak vertices
    for i in neighbors: # each vertice i
        neighs = neighbors[i]
        
        if len(neighs) < 2: # 0 or 1 neighbors => weak
            weak.append(i)
        else:
            triangle = False
            for j in neighs: # each of i's neighbors
                for k in neighs:
                    if k in neighbors[j]:
                        triangle = True
            if not triangle:
                weak.append(i)
    
    weak_vertices.append(weak)

# print weak vertices for each graph
for graph in weak_vertices:
    graph.sort()
    s = ""
    for v in graph:
        s += str(v) + " "
    print(s)