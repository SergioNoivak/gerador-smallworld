
from pprint import pprint
from Metricas import Metricas
import random as r
import networkx as nx
import matplotlib.pyplot as plt

class SmallWorld:
    def __init__(self) -> None:
        pass

    def GenerateSmallWorld(self,size,contador):
        isGerado = False
        vetor = []
        final_vector = []
        G=nx.DiGraph()
        while not isGerado:
            G=nx.DiGraph()
            for i in range(size):
                G.add_node(i)
            vetor = []
            n=size
            for i in [x for x in range(size)] :
                esq = ((i-1) % n + n) % n
                dir = ((i+1) % n + n) % n
                G.add_edge(i,dir)
                G.add_edge(i,esq)
            removes = []
            adds  = []
            metricas = Metricas()
            smallworldtest = G.edges
            with open("redesQuaisquer/"+str(contador)+".txt", 'a') as f:
                f.write("[\n")
                for item in G.edges:
                    f.write("%s,\n" % list(item))
                f.write("]\n")
            if(not metricas.isGrau2(G)):
                print("Elo inicial \n")
            for node in G.nodes:
                neighbors = G.neighbors(node)
                # print(list(neighbors))
                for neighbor in neighbors:
                    rand_num = r.random()
                    if(rand_num<0.1):
                    # if(1==1):
                       isGerado = True
                       elemento_sorteado= node
                       while elemento_sorteado == node or  elemento_sorteado in neighbors:
                           elemento_sorteado = r.randint(0,size-1)

                       removes.append([node,neighbor])
                       adds.append([node,elemento_sorteado])

                    # print(removes)                       
                    # print(adds)                       
            for remove in removes:
                G.remove_edge(remove[0],remove[1])
           
            for add in adds:
                G.add_edge(add[0],add[1])
           
            
        # metricas = Metricas()
        # metricas.isGrau2(G)
        # nx.draw(G, with_labels=True, node_size=0.03, node_color="skyblue", node_shape="s", alpha=0.5, linewidths=60)
        # plt.show()
        # plt.clf()
        # plt.cla()
        # plt.close()
        return G

        def __init__(self) -> None:
            pass
    