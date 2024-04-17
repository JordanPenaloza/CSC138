from graphs import graph1, graph2, graph3

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

def has_negative_cycle(graph):
    sum = 0
    for _, _, cost in graph:
         sum = sum + cost
    if sum < 0:
         return True
    return False

def choose_graph():
    choice = input("Which graph would you like to run (1, 2 or 3): ")
    if choice == "1":
        graph = graph1
    elif choice == "2":
        graph = graph2
    elif choice == "3":
        graph = graph3
    else:
        print("Bad choice try again ")
        choose_graph()
    return graph

def main():
    graph = choose_graph()
    num_nodes = max(max(node1, node2) for node1, node2, _ in graph)
    if has_negative_cycle(graph):
                print(f"Negative weight cycle detected")
    else:
        for source in range(1, num_nodes + 1):
            distances = bellman_ford(graph, source, num_nodes)
            print(f"Shortest distance from Node {source}: {distances}")

if __name__ == '__main__':
    main()

