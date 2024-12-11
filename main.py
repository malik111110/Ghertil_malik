# main.py
import random

def generate_complex_graph(num_nodes, max_connections=5, max_cost=20):
    graph = {i: [] for i in range(num_nodes)}
    for i in range(num_nodes):
        num_edges = random.randint(1, max_connections)
        for _ in range(num_edges):
            target = random.randint(0, num_nodes - 1)
            cost = random.randint(1, max_cost)
            if target != i:
                graph[i].append((target, (cost, random.random())))
    return graph

def ghertil_search(graph, start, end):
    visited = set()
    path = []
    costs = {node: float('inf') for node in graph}
    costs[start] = 0
    current = start

    while current != end:
        visited.add(current)
        path.append(current)
        for neighbor, (cost, _) in graph[current]:
            if neighbor not in visited:
                new_cost = costs[current] + cost
                if new_cost < costs[neighbor]:
                    costs[neighbor] = new_cost
        unvisited = {node: costs[node] for node in graph if node not in visited}
        if not unvisited:
            break
        current = min(unvisited, key=unvisited.get)

    path.append(end)
    return {
        "chemin": path,
        "coût_minimal": costs[end],
        "nœuds_ignorés": [node for node in graph if node not in visited],
    }

if __name__ == "__main__":
    num_nodes = 100
    graph = generate_complex_graph(num_nodes)
    result = ghertil_search(graph, 0, 99)
    print(f"Chemin Optimal : {result['chemin']}")
    print(f"Coût Minimal : {result['coût_minimal']}")
    print(f"Nœuds Ignorés : {result['nœuds_ignorés']}")
