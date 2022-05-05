from py4j.java_gateway import JavaGateway


def main():
    gateway = JavaGateway()
    entry = gateway.entry_point
    graph = entry.getGraph()
    graph.addEdge(1, 2)
    graph.addEdge(1, 3)
    graph.addEdge(1, 4)
    graph.addEdge(2, 4)
    graph2 = entry.getGraph()
    graph2.addEdge("wroclaw", "krakow")
    print(graph)
    print(graph2)
    print(graph.DFS(1))
    print(graph.BFS(1))


if __name__ == "__main__":
    main()
