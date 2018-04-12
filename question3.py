# Sorted parameter help from example on programiz.com
def take_second(elem):
    return elem[1]

def find_lowest(edges, visited_nodes):
    if len(edges):
        ordered = sorted(edges, key=take_second)
        for index, data in enumerate(ordered):
            if data[0] in visited_nodes:
                continue
            value = ordered.pop(index)
            return value


def question3(graph):
    if graph is {}:
        return None
    edge_list = []
    visited_nodes = []
    results = []
    adjacency_list = {}
    # Select the first node in the dictionary
    current_node = graph.iterkeys().next()
    # Initialize the first node to be visited
    visited_nodes.append(current_node)
    for index in range(0, len(graph)):
        # Parse to find their edges and append it to a list
        # Data would include the parent's node
        for edge in graph[current_node]:
            triple = (edge[0], edge[1], current_node)
            edge_list.append(triple)

        # Look into the list of edges to see there are any left
        # Find the edge with the lowest value
        value = find_lowest(edge_list, visited_nodes)
        # Switch current_node to the node with the lowest value
        current_node = value[0]
        visited_nodes.append(current_node)
        # Add results to a list of designated edges, nodes
        results.append(value)
        # When all nodes are visited, exit loop if necessary
        if len(visited_nodes) == len(graph):
            # Create the format as requested
            for result in results:
                adjacency_list[result[0]] = [(result[2], result[1])]
            break
        # Repeat, add all edges associated with that node
    return adjacency_list

# # Should print:
# {'A': [('B', 2)],
#  'B': [('C', 5)]}
# G = {
#     'A': [('B', 2)],
#     'B': [('A', 2), ('C', 5)],
#     'C': [('B', 5)]
# }
# print question3(G)

# # Should print:
# {'A': [('B', 3)],
# 'C': [('D', 2)],
# 'B': [('C', 5)],
# 'E': [('A', 1)]}
# G = {
#     'A': [('B', 3), ('E', 1)],
#     'B': [('A', 3), ('E', 4), ('C', 5)],
#     'C': [('B', 5), ('E', 6), ('D', 2)],
#     'D': [('C', 2), ('E', 7)],
#     'E': [('A', 1), ('D', 7)]
# }
# print question3(G)

# Should return None
G = {}
print question3(G)
