import pandas as pd
import sys
import networkx as nx
import csv
import matplotlib.pyplot as plt
from create_graph import cr_grph
G=nx.Graph()
(G,edge_data)=cr_grph()
bc_dict = dict(nx.betweenness_centrality(G))
ord_bet = dict(sorted(bc_dict.items(), key=lambda kv: kv[1],reverse = True))
bt_keys = []
bt_keys = list(bc_dict.keys())
print("Top 100 based on betweenness:")
"""
for i in range(100):
      print("ranking",bt_keys[i])
"""
with open('bc_dict_rec.csv', 'w') as csv_file:
      writer = csv.writer(csv_file)
      for key, value in bc_dict.items():
            writer.writerow([key, value])