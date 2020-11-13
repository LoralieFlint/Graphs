from util import Stack, Queue  # These may come in handy

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]


    def bft(self, starting_vertex):
        queue = Queue()
        queue.enqueue(starting_vertex)
        visited = set()

        while queue.size() > 0:
            current_vertex = queue.dequeue()

            if current_vertex not in visited:
                print(current_vertex)
                visited.add(current_vertex)

                neighbors = self.get_neighbors(current_vertex)
                for neighbor in neighbors:
                    queue.enqueue(neighbor)

    def dft(self, starting_vertex):
        stack = Stack()
        stack.push(starting_vertex)
        visited = set()

        while stack.size() > 0:
            current_path = stack.pop()

            if current_path not in visited:
                visited.add(current_path)
                print(current_path)

                for next_vertex in self.get_neighbors(current_path):
                    stack.push(next_vertex)

    def dft_recursive(self, starting_vertex):
        s = Stack()
        visited = set()
        def inner_dft(current):
            if current == None:
                return
            else:
                if current not in visited:
                    print(current)
                    visited.add(current)
                    for next_v in self.get_neighbors(current):
                        s.push(next_v)
                    inner_dft(s.pop())
                else:
                    inner_dft(s.pop())
        inner_dft(starting_vertex)


    def bfs(self, starting_vertex, destination_vertex):
        queue = Queue()
        visited_vertices = set()

        queue.enqueue({
            'current_vertex': starting_vertex,
            'path': [starting_vertex]
        })

        while queue.size() > 0:
            current_obj = queue.dequeue()
            current_path = current_obj['path']
            current_vertex = current_obj['current_vertex']

            if current_vertex not in visited_vertices:
                visited_vertices.add(current_vertex)

                if current_vertex == destination_vertex:
                    return current_path

                for vertex in self.get_neighbors(current_vertex):
                    new_path = list(current_path)
                    new_path.append(vertex)
                    queue.enqueue({
                        'current_vertex': vertex,
                        'path': new_path
                    })

    def dfs(self, starting_vertex, destination_vertex):
        stack = Stack()
        visited_vertices = set()

        stack.push({
            'current_vertex': starting_vertex,
            'path': [starting_vertex]
        })

        while stack.size() > 0:
            current_obj = stack.pop()
            current_path = current_obj['path']
            current_vertex = current_obj['current_vertex']

            if current_vertex not in visited_vertices:
                visited_vertices.add(current_vertex)

                if current_vertex == destination_vertex:
                    return current_path

                for vertex in self.get_neighbors(current_vertex):
                    new_path = list(current_path)
                    new_path.append(vertex)
                    stack.push({
                        'current_vertex': vertex,
                        'path': new_path
                    })

    def dfs_recursive(self, starting_vertex, destination_vertex):
        stack = Stack()
        visited = set()
        stack.push([starting_vertex])

        def dft_inner(current_path):
            current_vertex = current_path.pop()
            current_path.append(current_vertex)
            if current_vertex == destination_vertex:
                return current_path
            else:
                if current_vertex not in visited:
                    visited.add(current_vertex)
                    for neighbor in self.get_neighbors(current_vertex):
                        path_to_add = current_path + [neighbor]
                        stack.push(path_to_add)
                    return dft_inner(stack.pop())
                else:
                    return dft_inner(stack.pop())

        return dft_inner([starting_vertex])

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
