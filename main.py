from SmallWorld import SmallWorld
import networkx as nx
import matplotlib.pyplot as plt
from pprint import pprint
import random as r
from networkx.readwrite.json_graph import tree
from SmallWorld import SmallWorld
from Metricas import Metricas
from Algoritmos import Algoritmos
import json

metricas = Metricas()
algoritmos=Algoritmos()
tamanho = 100
estaConnectado = False
G = 1
x = 1
contador = 0
smallcont = 0
while contador<10:
    sm = SmallWorld()
    x = sm.GenerateSmallWorld(tamanho,smallcont)
    smallcont = smallcont+1
    G=x
    estaConnectado = algoritmos.isConnected(G)

    if estaConnectado:
        apl_coeficiente = metricas.APL(list(nx.all_pairs_shortest_path_length(G)),1000000)
        cc = nx.average_clustering(G)
        with open('APL.txt', 'a') as f:
            f.write("%s\n" % apl_coeficiente)
        with open('CC.txt', 'a') as f:
            f.write("%s\n" % cc)
        with open("redes/"+str(contador)+".txt", 'a') as f:
            f.write("[\n")
            for item in G.edges:
                f.write("%s,\n" % list(item))
            f.write("]\n")
        pos =nx.circular_layout(G,scale=0.5)
        plt.figure(3,figsize=(35,35)) 
        labels = {}
        edgeswidth =[]
        for i in range(100):
            labels[i]=i

        
        for i in range(200):
            edgeswidth.append(5)
        nx.draw_circular(G,node_size=1000,labels=labels,width=edgeswidth,arrowsize=50)
        plt.savefig("figuras/"+str(contador)+".png")
        plt.clf()
        plt.cla()
        plt.close()
        erro = not (metricas.isGrau2(G))
        if(erro):
            with open('logErros.txt', 'a') as f:
                f.write(json.dumps({"rede":contador,"erro":"Nao esta com grau 2","smallcont":smallcont-1}))
                f.write("\n")
        contador = contador + 1
  