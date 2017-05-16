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


def create_graph(n):
    # Identifiers of the nodes
    nodes = range(1, n+1)

    # Creating the Graph
    G = nx.Graph()
    G.add_nodes_from(nodes)

    return G


def r_regular_connected(n, r):
    # TODO: Add case for r odd
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

def check_r_regular(n, r, G, debug = False):
    for node in G.nodes():
        n = len(G.neighbors(node))
        if debug:
            print node, n
        if n != r:
            return False
    return True

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

def breadth_first_search (nodes, n, adj):
    visited=[]
    queue=[-1111]
    while (len(queue)!=0):
        if -1111 in queue:
            queue.remove(-1111)
        if (len(queue)!=0):
            actual=queue[0]
            queue.remove(actual)
        else:
            actual=nodes[0]
        if actual not in visited:
            visited.append(actual)
        for j in range(0,n):
            if (A[actual-1,j]==1 and j+1 not in queue and j+1 not in visited):
                queue.append(j+1)  
    return(len(visited)==len(nodes))
        

# Parameters for p_ER
'''
n, p = 10, 0.25

myGraph = p_ER(n, p)

print(myGraph.nodes())
print(len(myGraph.edges())/(n*(n-1)/2.0))

draw_our_graph(myGraph)
plt.show()   
'''

# Parameters for r_regular
times = 10

for x in range(times):
    n, r = 100, 20 

    trials = 1
    is_r_regular, myGraph = r_regular(n, r)

    while not is_r_regular:
        is_r_regular, myGraph = r_regular(n, r)
        trials += 1

    print("Trials", trials)
    print("Check r_regular:", check_r_regular(n, r, myGraph))

    draw_our_graph(myGraph)
    plt.show()       

    nodes=myGraph.nodes()
    A = nx.adjacency_matrix(myGraph)
    A = A.todense()
   
    print("Check connect BFS", breadth_first_search(nodes, n, A))
