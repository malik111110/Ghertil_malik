import tkinter as tk
import networkx as nx
import matplotlib.pyplot as plt
from main import generate_complex_graph, ghertil_search

class TransportNetworkInterface:
    def __init__(self, root, graph, result):
        self.root = root
        self.graph = graph
        self.result = result

        # Fenêtre principale
        self.root.title("Visualisation Réseau de Transport")
        self.root.geometry("800x600")

        # Bouton pour afficher le graphe
        tk.Button(root, text="Afficher le Graphe", command=self.display_graph).pack(pady=10)

        # Résultats
        self.display_results()

        # Bouton pour quitter
        tk.Button(root, text="Quitter", command=self.root.quit).pack(pady=10)

    def display_graph(self):
        G = nx.DiGraph()
        for node, neighbors in self.graph.items():
            for neighbor, (cost, _) in neighbors:
                G.add_edge(node, neighbor, weight=cost)

        pos = nx.spring_layout(G)
        plt.figure(figsize=(12, 8))

        # Dessiner les nœuds et les arêtes
        nx.draw_networkx_nodes(G, pos, node_size=700, node_color="lightblue")
        nx.draw_networkx_edges(G, pos, edgelist=G.edges(), arrowstyle="->", arrowsize=15)
        nx.draw_networkx_labels(G, pos, font_size=10)

        # Coûts des arêtes
        edge_labels = nx.get_edge_attributes(G, "weight")
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

        plt.title("Réseau de Transport")
        plt.show()

    def display_results(self):
        frame = tk.Frame(self.root)
        frame.pack(pady=20)

        tk.Label(frame, text="Résultats de l'Algorithme", font=("Arial", 16, "bold")).pack(pady=10)
        tk.Label(frame, text=f"Chemin Optimal : {self.result['chemin']}").pack()
        tk.Label(frame, text=f"Coût Minimal : {self.result['coût_minimal']}").pack()
        tk.Label(frame, text=f"Nœuds Ignorés : {self.result['nœuds_ignorés']}").pack()

if __name__ == "__main__":
    # Générer un graphe complexe
    num_nodes = 100
    graph = generate_complex_graph(num_nodes)

    # Calculer les résultats
    result = ghertil_search(graph, 0, 99)

    # Lancer l'interface graphique
    root = tk.Tk()
    app = TransportNetworkInterface(root, graph, result)
    root.mainloop()
