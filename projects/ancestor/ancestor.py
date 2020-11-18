
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
    ancient_one = dfs(ancestors, starting_node, 0)

    return ancient_one
