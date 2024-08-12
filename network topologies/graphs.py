import networkx as nx

G = nx.generators.trees.random_tree(n=50)
nx.write_pajek(G, "tree.net")