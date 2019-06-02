import pandas as pd
import sys
import networkx as nx
import csv
import copy
import random
import matplotlib.pyplot as plt
from create_graph import cr_grph
from closeness import cc_Dict_order
from bc_calc import ord_bet
G=nx.Graph()
(G,edge_data)=cr_grph()
H=copy.deepcopy(G)
J=copy.deepcopy(G)
"""Important noodes based on betweenness centrality"""
imp_nod_bet = []
imp_bet = []
imp_nod_bet = list(cc_Dict_order.keys())
"""Important noodes based on closeness centrality"""
imp_nod_clo = []
imp_clo = []
imp_nod_clo= list(ord_bet.keys())

for i in range(100):
      imp_bet = imp_nod_bet[i]  
      J.node[imp_bet]['color']='green'
for i in range(100):
      imp_clo = imp_nod_clo[i]

print("intersection",list(set(imp_bet).intersection(imp_clo)))
print("--------", nx.info(J))
print("Color changed")
nx.write_graphml(J,"important.graphml")