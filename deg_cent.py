import pandas as pd
import sys
import networkx as nx
import csv
import matplotlib.pyplot as plt
from create_graph import cr_grph
G=nx.Graph()
(G,edge_data)=cr_grph()
#print("NODES:")
#print(list(G))
sort_Deg_Dict = sorted(G.degree, key=lambda x: x[1], reverse=True)
#print("Degrees",sort_Deg_Dict)
deg_cc_Dict = dict(nx.degree_centrality(G))
deg_cc_Dict_or = dict(sorted(deg_cc_Dict.items(), key=lambda kv: kv[1],reverse = True))
deg_keys = []
deg_keys = list(deg_cc_Dict_or.keys())
for i in range(2):
    print(deg_keys[i])
with open('deg_dict_rec.csv', 'w') as csv_file:
      writer = csv.writer(csv_file)
      for key, value in deg_cc_Dict.items():
            writer.writerow([key, value])