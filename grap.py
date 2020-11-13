# SLL
class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class BinarySearchTreeNode:
      def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Binary search tree traversals
# BFS (breadth first search)
# DFS (deapth first search)

class GraphNode:
      def __init__(self, value):
        self.value = "B"

        # options: dict, array, set
        self.connections = set("A", "B", "C", "D")

        # B's connections 
        self.connections = set("A", "C", "D")
        # A's connections 
        self.connections = set("B")
        # D's connections 
        self.connections = set(None)



# outbound vs inbound connections
# Graph terminology for 2 way vs 1 way connection
## undirected graph vs directed graph 
## ( FB & LinkedIn ) vs ( Instagram twitter TikTok )

# graph traversals
# DFT, stack 
# check every node once, check every connection once 

# make a stack
stack = Stack()
# make a set to track visited
visited = set("A")
# put the start note into the stack 
# while the stack isnt empty 
# pop off the top of the stack, this is our current node
current_node = "a"

# check if we have visited this node yet

# if not, add it to our visited list 

# and add each of its neighbors to our stack 


# TIME COMPLEXITY
### how many times did we visit each node? once
### how many times did we check each connection? once

## O(number of nodes + number of connections)
## O(n+m)
## so linear


# BFT que
q = Que("B")

# make a set to track visited 
visited = set("A", "B", "C")

# enque the start node

# while our que isnt empty 
## deque from the front of the line, this is our current node 
current_node = "D"

# check if we visited here yet 
# if not add to visited 
# get its neighbors, for each, add its neighbors
neighbors = set("E")


# TIME COMPLEXITY
### how many times did we visit every vertex? visit every edge once
## O( n + m )
## O(node + edge)
## so linear

# DFT VS BFT 
## same time complexity each just as fast
## DFT can be done recursively 
## BFT can find shortest path