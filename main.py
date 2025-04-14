class Grafo:
    def __init__(self, vertices, orientado=False):
        self.vertices = vertices
        self.orientado = orientado
        self.adj = {v: [] for v in vertices}

    def adicionar_aresta(self, u, v):
        self.adj[u].append(v)
        if not self.orientado:
            self.adj[v].append(u)

def caminho_hamiltoniano(grafo):
    caminho = []
    visitados = {v: False for v in grafo.vertices}

    def backtrack(atual):
        caminho.append(atual)
        visitados[atual] = True

        # Verifica se encontrou um caminho hamiltoniano
        if len(caminho) == len(grafo.vertices):
            return True

        for vizinho in grafo.adj[atual]:
            if not visitados[vizinho]:
                if backtrack(vizinho):
                    return True

        # Backtrack
        caminho.pop()
        visitados[atual] = False
        return False

    for vertice in grafo.vertices:
        if backtrack(vertice):
            return caminho
        caminho.clear()
        visitados = {v: False for v in grafo.vertices}
    
    return None

def main():
    vertices_no = ['A', 'B', 'C', 'D', 'E', 'F']
    arestas_no = [
        ('A', 'B'), ('A', 'C'), 
        ('B', 'D'), ('C', 'D'), 
        ('D', 'E'), ('E', 'F'), 
        ('F', 'A'), ('B', 'F')
    ]

    g_no = Grafo(vertices_no, orientado=False) # grafo não orientado
    for u, v in arestas_no:
        g_no.adicionar_aresta(u, v)

    print("\n[Grafo Não Orientado]")
    print("Vértices:", vertices_no)
    print("Arestas:", arestas_no)
    caminho = caminho_hamiltoniano(g_no)
    print("\nCaminho Hamiltoniano encontrado:", caminho if caminho else "Nenhum")

    vertices_or = ['K', 'L', 'M', 'N', 'O', 'P', 'Q']
    arestas_or = [
        ('K', 'L'), ('K', 'M'),
        ('L', 'N'), ('M', 'N'),
        ('N', 'O'), ('N', 'P'),
        ('O', 'Q'), ('P', 'Q'),
        ('Q', 'L')
    ]

    g_or = Grafo(vertices_or, orientado=True)
    for u, v in arestas_or:
        g_or.adicionar_aresta(u, v)

    print("\n[Grafo Orientado]")
    print("Vértices:", vertices_or)
    print("Arestas:", arestas_or)
    caminho = caminho_hamiltoniano(g_or)
    print("\nCaminho Hamiltoniano encontrado:", caminho if caminho else "Nenhum")

    return

if __name__ == "__main__":
    main()