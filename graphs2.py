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

# Solving ( ALMOST ) any Graphs problem
'''
0. Spot that you might use a graph to solve it
- shortest path
- spot that there are things connected to other things
'''
'''
1. Describe the problem using graphs terminology
- what are my nodes here?
- what are my edges? aka when is there an edge, when is a node connected to another node? when not?
'''
'''
2. build your graph, or write get neighbors
'''
'''
3. choose your fighter, traverse your graph
'''

''' 
Given two worde (begin_word and end_word), and a dictionarys word list,
return the shortest transformationsequencefrom begin_word to end_word, such that:

Only one letter can be changed at a time 

Each transformation word must exist in the word list. Note that begin_word is not a transformed word.

note:
return None if there is no such transformation sequence
all words contain only lowercaseaplhabetic characters 
you may assume no duplicatesin the word list
you may assume begin_word and end_word are non empty and are not the same

Sample:
begin_word: "hit"
end_word: "cog"

begin_word: "sail"
end_word: "boat"
'''


f= open(something, 'f')
giant_list_of_words = f.read('\n')
f.close()

# BFS
def bfs(start_node, target_node):
    q = Queue()
    visited = set()
    q.enqueue([start_node])
    while q.size() > 0:
        current_path = q.dequeue()
        current_node = current_path[-1]
        if current_node == target_node:
            return current_path
        if current_node not in visited:
            visited.add(current_node)
            neighbors = getNeighbors(current_node)
            for neighbor in neighbors:
                path_copy = list(current_path)
                path_copy.append(neighbor)
                q.enqueue(path_copy)
                
begin_word = "hit"
end_word = "cog"
print(bfs(begin_word, end_word))
begin_word = "sail"
end_word = "boat"
print(bfs(begin_word, end_word))



#### do not try an impliment this way 
### worst time complexity EVER!
'''
for word in giant_list_of_words:
        if word not in my_graph.verticies:
            my_graph.add_node(word)
            for other_word in giant_list_of_words:
                if is_edge(word, other_word):
                    my_graph.add_edge(word, other_word)
'''