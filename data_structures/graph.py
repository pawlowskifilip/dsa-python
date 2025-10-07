class Graph:
    def __init__(self):
        self.graph = {}

    def add(self, from_vertex, to_vertex):
        # and edge
        if from_vertex in self.graph:
            self.graph[from_vertex].append(to_vertex)

        # add vertex
        else:
            self.graph[from_vertex] = [to_vertex]

    def remove(self, vertex):
        if vertex in self.graph:
            del self.graph[vertex]
        for vertices in self.graph.values():
            if vertex in vertices:
                vertices.remove(vertex)

    def display(self):
        for vertex in self.graph:
            adjacent_vertices = ", ".join(map(str, self.graph[vertex]))
            print(f"{vertex} --> {adjacent_vertices}")

    def bfs(self, start_vertex):
        if start_vertex not in self.graph:
            return []

        queue = [start_vertex]
        traversal = []

        while queue:
            vertex = queue.pop(0)
            if vertex not in traversal:
                traversal.append(vertex)
                if vertex in self.graph:
                    queue.extend(self.graph[vertex])

        return traversal

    def dfs(self, start_vertex):
        if start_vertex not in self.graph:
            return []

        stack = [start_vertex]
        traversal = []

        while stack:
            vertex = stack.pop()
            if vertex not in traversal:
                traversal.append(vertex)
                if vertex in self.graph:
                    stack.extend(reversed(self.graph[vertex]))

        return traversal


g = Graph()
g.add(1, 2)
g.add(1, 3)
g.add(2, 4)
g.add(2, 5)
g.add(4, 5)
g.display()
print(g.graph)
print(g.bfs(1))
print(g.dfs(1))
