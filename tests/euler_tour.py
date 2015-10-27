def find_eulerian_tour(graph):
    tour = []

    current_vertex = graph[0][0]
    tour.append(current_vertex)

    while len(graph) > 0:
        print(graph, current_vertex)
        for edge in graph:
            if current_vertex in edge:
                if edge[0] == current_vertex:
                    current_vertex = edge[1]
                else:
                    current_vertex = edge[0]

                graph.remove(edge)
                tour.append(current_vertex)
                break
        else:
            # Edit to account for case no tour is possible
            return False
    return tour

graph = [(1, 2), (2, 3), (3, 1), (3, 4), (4, 3)]
print(find_eulerian_tour(graph))