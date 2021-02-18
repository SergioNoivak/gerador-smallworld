import networkx as nx

class Algoritmos:
    def __init__(self) -> None:
        pass    
    
    def isConnected(self,G):
        isConnected = False
        for node in G.nodes:
            lista = list(nx.dfs_edges(G,source=node))
            if self.isConnectedLocal(node,lista,len(G.nodes)):
                return True
        return False



    def isConnectedLocal(self,node,edges,sizeNodes):
        isConnected = False
        percorrido = {}
        for i in range(sizeNodes):
             percorrido[i] = False
        if edges:
            percorrido[node] = True   
            for edge in edges:
                percorrido[edge[1]] = True
                # pprint(edges)

            for i in range(sizeNodes):
                     if not percorrido[i]:
                         return False
            return True
        else:
            return False
