from graphs import graph2

def bellman_ford(graph, source, num_nodes):
    distances = [float("inf")] * (num_nodes + 1)
    distances[source] = 0

    for _ in range(num_nodes - 1):
        for src, dest, cost in graph:
            if distances[src] != float("inf") and distances[src] + cost < distances[dest]:
                distances[dest] = distances[src] + cost
            if distances[dest] != float("inf") and distances[dest] + cost < distances[src]:
                distances[src] = distances[dest] + cost
                
    return distances[1:]

def has_negative_cycle(distances):
    if sum(distances) < 0:
        return True
    return False

def main():
    num_nodes = max(max(node1, node2) for node1, node2, _ in graph2)
    for source in range(1, num_nodes + 1):
        distances = bellman_ford(graph2, source, num_nodes)
        if has_negative_cycle(distances):
                print(f"Negative weight cycle detected")
                break
        print(f"Shortest distance from Node {source}: {distances}")

if __name__ == '__main__':
    main()

