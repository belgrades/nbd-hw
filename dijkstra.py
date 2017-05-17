import networkx as nx
from itertools import combinations
from random import random, randrange, sample
import matplotlib.pyplot as plt
import numpy as np
import pprint as pp

def draw_our_graph(G):
    nx.draw(G, with_labels = True)


def create_graph(n):
    # Identifiers of the nodes
    nodes = range(1, n+1)

    # Creating the Graph
    G = nx.Graph()
    G.add_nodes_from(nodes)

    return G

def r_regular(n, r, debug = False):
    G = create_graph(n)

    # Random order for creating graph
    random_order = sample(G.nodes(), n)

    for idx, x in enumerate(random_order):
        # Check for the neighbors of x
        neighbors = G.neighbors(x)

        # We denote k as the number of neighbors for node x
        k = len(neighbors)

        # If the actual node x has r neighbors, continue to next node
        if k == r:
            continue

        # Set of possible new nodes that could be connected to x
        possibles = list(set(G.nodes()).difference(set(neighbors)).difference(set([x]))) 

        while k != r:
            # Select randomly one element
            p = sample(possibles, 1)[0]
            
            # Remove the element
            possibles.remove(p)

            # If neighbors(p) add edge (x, p) and set k = len(neighbors(x))
            if len(G.neighbors(p)) < r:
                G.add_edge(x, p)
                k = len(G.neighbors(x))

            # If empty(possibles) == T and k < r no more possibilities
            if possibles == [] and k < r:
                return False, G
    return True, G           
    

def p_ER(n, p):
    # Identifiers of the nodes
    nodes = range(1, n+1)

    # Creating the Graph
    G = nx.Graph()
    G.add_nodes_from(nodes)
    
    # For every combination (x,y) in nodes() (x, y) in edges with probability p
    for edge in combinations(G.nodes(), 2):
        if random() < p:
            # same as G.add_edge(edge[0], edge[1])
            G.add_edge(*edge)

    return G


def dijkstra(G, u, v):
    '''
    Find all possible paths from u to all nodes
    '''

    Q, dist, prev = [], {}, {}

    # Initialize structures
    for vertex in G.nodes():
        Q.append(vertex)
        dist[vertex] = np.inf
        prev[vertex] = []

    # Add u to Q
    dist[u] = 0
    prev[u] = [u]

    # print(Q)

    while Q:
        # Minimum distance in Q
        min_dis = min(d for v, d in dist.items() if v in Q)

        # Select randomly from all possible options
        a = sample([q for q in Q if dist[q] == min_dis], 1)[0]
        # print(a)
       
        Q.remove(a)
        # print(Q)
        for neighbor in G.neighbors(a):
          #  print(neighbor)
            if dist[a]+1 < dist[neighbor]:
                # New distance, clear neighbors. Set distance
                prev[neighbor] = [a]
                dist[neighbor] = dist[a] + 1
            elif dist[a]+1 == dist[neighbor]:
                # We have a tie, add to prev a
                prev[neighbor].append(a)


        if v == a:
            Q = []
                
    return dist, prev

def create_paths(prev, dist, u, v):
    # Create all the paths from u to v
    paths, Q, actual = [[v]], [v], v

    if dist[v] == np.inf:
        return []

    while actual != u:
        # Select actual node as a queue
        # print(Q)
        # print(actual)
        actual = Q[0]

        if actual == u:
            break

        # Remove actual node from Q
        Q.remove(actual)

        # Retrieve all paths which last node is actual
        paths_actual = [path for path in paths if path[-1] == actual]

        # Remove this paths from paths structure
        for path in paths_actual:
            paths.remove(path)

        # Create a new path for every previous of actual
        # Append p in Q
        for p in prev[actual]:
            Q.append(p)
            for path in paths_actual:
                paths.append(path+[p])

    for path in paths:
        path.reverse()
    
    return paths
            

# Parameters for p_ER
'''
n, p = 10, 0.25

myGraph = p_ER(n, p)
'''

times = 10

for x in range(times):
    n, r = 100, 16 

    trials = 1
    is_r_regular, myGraph = r_regular(n, r)

    while not is_r_regular:
        is_r_regular, myGraph = r_regular(n, r)
        trials += 1

    print("Trials", trials)
    #print("Check r_regular:", check_r_regular(n, r, myGraph))

    draw_our_graph(myGraph)
    plt.show()
    u, v = 1, 4
    dist, prev = dijkstra(myGraph, u, v)

    pretty = pp.PrettyPrinter(indent=3)

#    pretty.pprint(prev)
#    pretty.pprint(dist)
    pretty.pprint(create_paths(prev, dist, u, v))



n = 4

myGraph = create_graph(n)
myGraph.add_edge(1,2)
myGraph.add_edge(1,3)
myGraph.add_edge(3,2)

n, p = 200, 0.05

myGraph = p_ER(n, p)

print(myGraph.nodes())
print(len(myGraph.edges())/(n*(n-1)/2.0))

draw_our_graph(myGraph)
plt.show()   

u, v = 1, 4
dist, prev = dijkstra(myGraph, u, v)

pretty = pp.PrettyPrinter(indent=3)

pretty.pprint(prev)
pretty.pprint(dist)
pretty.pprint(create_paths(prev, dist, u, v))
