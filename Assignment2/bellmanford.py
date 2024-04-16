graph = [
(1, 2, 2),
(1, 3, 7),
(2, 3, 1),
]
num_nodes = len(graph)

def bellman_ford (graph, source):
    dist = [float('inf')] * (num_nodes + 1)
    dist[source] = 0
    
    for _ in range(num_nodes - 1):
        for src, dest, cost in graph:
            if dist[src] != float('inf') and dist[src] + cost < dist[dest]:
                dist[dest] = dist[src] + cost
    return dist[1:]

for source in range(1, num_nodes + 1):
    distances = bellman_ford(graph, source)
    print(f"Shortest distances from node {source}: {distances}")
                
    
    
    
