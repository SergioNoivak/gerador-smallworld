
class Metricas:
    def __init__(self) -> None:
        pass

    def APL(self,matrix,size):
        d = 0
        for i in matrix:
            for key in i[1]:
                d = d+i[1][key]
        return d/(size*(size-1))


    def CC(self,G):
        cc = 0
        for node in G.nodes:
            c_i = 0
            arestas_consideradas = 0
            neighbors=G.neighbors(node)
            for neighbor in neighbors:
                # print(neighbor)
                vizinhos_distantes = G.neighbors(neighbor)
                for vizinho_distante in vizinhos_distantes:
                    if vizinho_distante in neighbors:
                        # print("somado")
                        arestas_consideradas = arestas_consideradas+1 
            # print("\n")
            # print(arestas_consideradas)
            c_i = arestas_consideradas/G.degree[node]
            # print(c_i)

    def isGrau2(self,G):
        marcados = {}
        for node in G.nodes:
            marcados[node] = 0
        for edge in G.edges:
            marcados[edge[0]] = marcados[edge[0]]+1

        certo = True
        for key in marcados:
            if(marcados[key] != 2):
                print(G.edges)
                print(G.nodes)
                print(key)
                print("\n")
                print(marcados[key])
                print(marcados)
                return False
        return certo