import networkx as nx
from itertools import combinations
from random import random, randrange, sample
import matplotlib.pyplot as plt

'''
Requeriments:
    pip install networkx
    pip install matplotlib
'''

def draw_our_graph(G):
    nx.draw(G, with_labels = True)

def r_regular(n, r):
    def get_index(idx, r, n):
        # IF we are at node 0 and r = 4,  we need to add nodes 1 and 2. (Remember r/2)
        # But if we are at node n - 1, we need to add nodes n and 0. Therefore,
        # if idx + r exceeds n - 1 we add idx + r - n
        return idx + r if idx + r < n else idx + r - n
    
    # Input
    if n == r or n*r % 2 == 1:
        print "Input error"
        return -1    
    
    # Identifiers of the nodes
    nodes = range(1, n+1)

    # Creating the Graph
    G = nx.Graph()
    G.add_nodes_from(nodes)

    # Generate r-regular graph
    # We need to create nr edges
    # First we need a random order of the nodes
    random_order = sample(G.nodes(), n)

    for idx, x in enumerate(random_order):
        # We add r/2 edges on the "right" of every node
        # As we have n edges, we'll have n*r edges in the end
        for idy in range(1, int(r/2)+1):
            idz = get_index(idx, idy, n)
            G.add_edge(x, random_order[idz])
    
    return G 


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

# Parameters for p_ER
n, p = 10, 0.25

myGraph = p_ER(n, p)

print(myGraph.nodes())
print(len(myGraph.edges())/(n*(n-1)/2.0))
draw_our_graph(myGraph)
plt.show()   


# Parameters for r_regular
n, r = 8, 4 

myGraph = r_regular(n, r)

draw_our_graph(myGraph)
plt.show()       
