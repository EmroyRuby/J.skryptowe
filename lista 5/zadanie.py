from py4j.java_gateway import JavaGateway


def main():
    gateway = JavaGateway()
    graph = gateway.entry_point.getGraph()
    graph.addEdge(1, 2)
    graph.addEdge(1, 3)
    graph.addEdge(1, 4)
    graph.addEdge(2, 4)
    print(graph)
    print(graph.DFS(1))
    print(graph.BFS(1))


if __name__ == "__main__":
    main()