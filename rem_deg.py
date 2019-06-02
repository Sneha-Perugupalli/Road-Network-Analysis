import pandas as pd
import sys
import networkx as nx
import csv
import copy
import random
import numpy as np
from random import choice
from itertools import islice
import matplotlib.pyplot as plt
from create_graph import cr_grph
from deg_cent import deg_cc_Dict_or
G=nx.Graph()
(G,edge_data)=cr_grph()
H=copy.deepcopy(G)
J1=copy.deepcopy(G)
J2=copy.deepcopy(G)
""" 1 simple shortest path"""
def effected_shortest_paths(G, source, target, k, weight=None):
       return list(islice(nx.shortest_simple_paths(G, source, target, weight=weight), k))
routeDict = {}
to_rem_deg = list(deg_cc_Dict_or.keys())
print("Number of nodes", len(list(J1.nodes())))
    
for i in range(1045):
      rem = to_rem_deg[i]
      #print("To rem", to_rem[i])
      J2.remove_node(to_rem_deg[i])

print("After Removal", len(list(J2.nodes())))
""" Select Two Nodes """
s = np.random.choice(J2.nodes())
t = np.random.choice(J2.nodes()) 
print("Source: ", s)
print("Target: ", t)

sp_list = []
sp_list_rem = []

if nx.has_path(J1, s, t):
      for path in effected_shortest_paths(J1, s, t, 1):
            total_length = 1
            for i in range(len(path)-1):
                  n = path[i]
                  J1.node[n]['color']='blue'
                  J1.add_path(n,color= 'blue' )
                  total_length += 1
            print("Shortest path before removal")
            print('{}: {}'.format(path, total_length))
      nx.write_graphml(J1,"SP_Deg_Bef_removal.graphml")
else:
      print("No Path between these nodes, Kindly run again!!")
if nx.has_path(J2, s, t):      
      for path in effected_shortest_paths(J2, s, t, 1):
            total_length = 1
            for i in range(len(path)-1):
                  n = path[i]
                  J2.node[n]['color']='red'
                  J2.add_path(n,color= 'red' )
                  total_length += 1
            print("Shortest path After removal")
            print('{}: {}'.format(path, total_length))
      nx.write_graphml(J2,"SP_Deg_Aft_removal.graphml")
else:
      print("No Path between these nodes, Kindly run again!!")

print("After Removal - 2 ", len(list(J2.nodes())))