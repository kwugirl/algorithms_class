from sys import argv

script, filename = argv

txt = open(filename)

# run through file to get out all the numbers in the list
# each line looks like "1\t2,3\t3,4\t\n"
graph_dict = {}
for line in txt:
    line = line.rstrip().split('\t')  # strip off trailing whitespaces, split at tabs
    key = int(line.pop(0))
    graph_dict[key] = {}

    for edge in line:
        pair = edge.split(',')
        graph_dict.get(key)[int(pair[0])] = int(pair[1])

txt.close()

shortest_path = {1: 0}
candidate_length = 0

while candidate_length < float("inf"):  # this trickiness is to deal with if graph contains nodes that are unreachable from source node and you get stuck
    candidate_length = float("inf")

    for v in shortest_path:
        edges = graph_dict.get(v)

        if edges is None:  # this is if vertex is sink vertex in graph, no edges leading out from it
            pass
        elif len(edges) == 0:
            del graph_dict[v]
        else:
            for e in edges:
                e_delete = []
                if e in shortest_path:
                    e_delete.append(e)
                elif edges[e] + shortest_path[v] < candidate_length:
                    candidate_length = edges[e] + shortest_path[v]
                    candidate_head = e
                    candidate_tail = v

            for e in e_delete:
                del edges[e]

    if candidate_length < float("inf"):
        shortest_path[candidate_head] = candidate_length
        del graph_dict[candidate_tail][candidate_head]

# print shortest_path
# destinations = [2, 4, 6]

destinations = [7,37,59,82,99,115,133,165,188,197]
for v in destinations:
    print shortest_path.setdefault(v,1000000), ",",  # using setdefault in case node is one that wasn't reachable from source node and therefore should have path length of 1000000 according to the problem
