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
Ei_cc_Dict = dict(nx.eigenvector_centrality(G))
#print("---------",Ei_cc_Dict)
Ei_cc_Dict_or = dict(sorted(Ei_cc_Dict.items(), key=lambda kv: kv[1],reverse = True))
#print("Ordered eigen vector centrality Nodes",Ei_cc_Dict_or)
#print("Top 100 based on Eigen vector centrality")
eig_keys = []
eig_keys = list(Ei_cc_Dict.keys())
#for i in range(100):
#    print("Eigen", eig_keys[i])
with open('ei_dict_new.csv', 'w') as csv_file:
      writer = csv.writer(csv_file)
      for key, value in Ei_cc_Dict.items():
            writer.writerow([key, value])