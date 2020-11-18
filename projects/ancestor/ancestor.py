class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

# notes from graphs 3 lecture 
def dfs(ancestors, node, distance):
    parent = getNeighbors(node)
    
    if len(parents) == 0:
        return (node, distance)

    ancient_one = (node, distance)
    for parent in parents:
        node_pair = dfs(ancestors, parent, distance)

        if node_pair[i] > distance:
            ancient_one = node_pair

    return ancient_one


def earliest_ancestor(ancestors, starting_node):
    queue = Queue()
    path = [starting_node]
    queue.enqueue(path)
    visited = set()
    while queue.size() > 0:

        current_pair = queue.dequeue()
        neighbor = []

        for i in current_pair:
            for pairs in ancestors:
                if pairs[1] == i and i not in visited:
                    visited.add(i)
                    neighbor.append(pairs[0])
                    queue.enqueue(neighbor)
        
        if len(neighbor) <= 0:
            if current_pair[0] == starting_node:
                return -1
            else:
                return current_pair[0]
