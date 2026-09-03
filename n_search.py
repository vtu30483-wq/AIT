graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C', 'E'],
    'E': ['D']
}

def can_color(vertex, color, colors):
    for neighbor in graph[vertex]:
        if colors.get(neighbor) == color:
            return False
    return True

def graph_coloring(vertices, colors):
    if len(colors) == len(vertices):
        return True

    vertex = vertices[len(colors)]

    for color in ["Red", "Blue"]:
        if can_color(vertex, color, colors):
            colors[vertex] = color

            if graph_coloring(vertices, colors):
                return True

            del colors[vertex]

    return False


vertices = list(graph.keys())
colors = {}

if graph_coloring(vertices, colors):
    print("Minimum colors: 2")
    for vertex in vertices:
        print(vertex, "->", colors[vertex])
