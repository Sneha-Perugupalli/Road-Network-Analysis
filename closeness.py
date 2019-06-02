import pandas as pd
import sys
import networkx as nx
import csv
import matplotlib.pyplot as plt
from create_graph import cr_grph
G=nx.Graph()
(G, edge_data)=cr_grph()
cc_Dict = dict(nx.closeness_centrality(G)) 
cc_Dict_order = dict(sorted(cc_Dict.items(), key=lambda kv: kv[1],reverse = True))
keys = []
keys = list(cc_Dict_order.keys())
"""
for i in range(100):
      print("ranking",keys[i])
"""
with open('closeness_dict_rec.csv', 'w') as csv_file:
      writer = csv.writer(csv_file)
      for key, value in cc_Dict.items():
            writer.writerow([key, value])