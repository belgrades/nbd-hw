import networkx as nx
from itertools import combinations
from random import random, randrange
import matplotlib.pyplot as plt


def draw_our_graph(G):
    nx.draw(G)

def r_regular(n, r):
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

    possibles = list(combinations(G.nodes(), 2))

    while len(G.edges()) < n*r:
        # Randomly select an edge from possibles
        idx = randrange(0, len(possibles))
        edge = possibles[idx]
        
        # Check if edge can be in G
        if len(G.neighbors(edge[0])) < r and len(G.neighbors(edge[1])) < r:
            G.add_edge(*edge)
            possibles.pop(idx)
        nx.draw(G)
        plt.show()
    
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
            G.add_edge(*edge)

    return G

n, p = 10, 0.25

myGraph = p_ER(n, p)

print(myGraph.nodes())
print(len(myGraph.edges())/(n*(n-1)/2.0))
draw_our_graph(myGraph)
plt.show()   

n, r = 6, 2

myGraph = r_regular(n, r)

draw_our_graph(myGraph)
plt.show()       
