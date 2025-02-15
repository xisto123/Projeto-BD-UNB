import matplotlib.pyplot as plt
import networkx as nx

# Cria um grafo direcionado
G = nx.DiGraph()

# Adiciona nós (camadas)
G.add_node("Interface Gráfica (Tkinter)")
G.add_node("Serviços (Services)")
G.add_node("Modelos (Models)")
G.add_node("Persistência (Database)")
G.add_node("Banco de Dados (PostgreSQL)")

# Adiciona as arestas (fluxo de dados/controle)
G.add_edge("Interface Gráfica (Tkinter)", "Serviços (Services)")
G.add_edge("Serviços (Services)", "Modelos (Models)")
G.add_edge("Modelos (Models)", "Persistência (Database)")
G.add_edge("Persistência (Database)", "Banco de Dados (PostgreSQL)")

# Define posições manuais para os nós
pos = {
    "Interface Gráfica (Tkinter)": (0, 4),
    "Serviços (Services)": (0, 3),
    "Modelos (Models)": (0, 2),
    "Persistência (Database)": (0, 1),
    "Banco de Dados (PostgreSQL)": (0, 0)
}

# Define cores para cada nó
colors = {
    "Interface Gráfica (Tkinter)": "lightblue",
    "Serviços (Services)": "lightgreen",
    "Modelos (Models)": "lightcoral",
    "Persistência (Database)": "lightyellow",
    "Banco de Dados (PostgreSQL)": "lightgray"
}
node_colors = [colors[node] for node in G.nodes()]

# Cria a figura e o eixo
fig, ax = plt.subplots(figsize=(8, 6))

# Desenha os nós como círculos
nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=3000,
                       node_shape='o', linewidths=2, edgecolors='black')

# Desenha as arestas com setas
nx.draw_networkx_edges(G, pos, arrows=True, arrowstyle='-|>', arrowsize=20, width=2)

# Define o offset para os rótulos (ajuste este valor conforme necessário)
offset = 1.1  # Quanto mais negativo, mais para a esquerda os rótulos serão posicionados

# Calcula as posições dos rótulos com o offset aplicado
pos_labels = {node: (x + offset, y) for node, (x, y) in pos.items()}

# Desenha os rótulos
nx.draw_networkx_labels(G, pos_labels, font_size=10, font_weight='bold')

# Ajusta os limites dos eixos para garantir que os rótulos fiquem visíveis
ax.set_xlim(-2, 3)
ax.set_ylim(-1, 5)
ax.axis("off")
plt.tight_layout()

pdf_path = "diagrama_mapeamento.pdf"
plt.savefig(pdf_path, format="pdf", bbox_inches="tight")
