from __future__ import division
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import sys
import csv
from create_graph import cr_grph
G=nx.Graph()
(G, edge_data)=cr_grph()
clust_Dict=[]

def clust_coeff(G):
    clust_Dict = {}
    for n in G:
        node_neighbours = []
        mutual_nodes = []
        for neighbour in G.neighbors(n):
            node_neighbours.append(neighbour)
        for neighbour in G.neighbors(n):
            for mutual_neighbour in G.neighbors(neighbour):
                if mutual_neighbour in node_neighbours:
                    mutual_nodes.append(mutual_neighbour)
        mutual_nodes = list((mutual_nodes))
        clusteringCoefficient = 0.0
        if len(list(mutual_nodes)):
            if len(list((node_neighbours))) == 1: break
            clusteringCoefficient = (2.0 * float(len(list(mutual_nodes))))/((float(len(list((node_neighbours)))) * (float(len(list((node_neighbours))))))-1)

        clust_Dict[n] = clusteringCoefficient
    return clust_Dict

clust_coeff(G)
#clust_coeff(G)
print("clusterin Coefficient is: ", clust_coeff(G))
# print 1 test value
clust_Dict = clust_coeff(G)
with open('clus_dict_rec.csv', 'w') as csv_file:
      writer = csv.writer(csv_file)
      for key, value in clust_Dict.items():
            writer.writerow([key, value])