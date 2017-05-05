import networkx as nx
from itertools import combinations
from random import random, randrange, sample
import matplotlib.pyplot as plt


def draw_our_graph(G):
    nx.draw(G, with_labels = True)

def r_regular(n, r):
    def get_index(idx, r, n):
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

    random_order = sample(G.nodes(), n)

    for idx, x in enumerate(random_order):
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

n, p = 10, 0.25

myGraph = p_ER(n, p)

print(myGraph.nodes())
print(len(myGraph.edges())/(n*(n-1)/2.0))
draw_our_graph(myGraph)
plt.show()   

n, r = 8, 4 

myGraph = r_regular(n, r)

draw_our_graph(myGraph)
plt.show()       
