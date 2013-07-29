import random
from sys import argv

script, filename = argv

txt = open(filename)

# run through file to get out all the numbers in the list
# each line looks like "1\t2\t3\t\n"
graph_dict = {}
for line in txt:
    line = line.rstrip().split('\t')  # strip off trailing whitespaces, split at tabs
    for i in range(len(line)):
        line[i] = int(line[i])
    graph_dict[line.pop(0)] = line

txt.close()

# print graph_dict


def find_min_cut(graph_dict):

    while len(graph_dict) > 2:
        edge_tuple = choose_rand_edge(graph_dict)
        graph_dict = contract_edge(graph_dict, edge_tuple)

    vertices = graph_dict.keys()

    return len(graph_dict[vertices[0]])


def choose_rand_edge(graph_dict):
    first_vertex = random.choice(graph_dict.keys())
    second_vertex = random.choice(graph_dict[first_vertex])

    return (first_vertex, second_vertex)


def contract_edge(graph_dict, edge_tuple):
    first_vertex = edge_tuple[0]
    second_vertex = edge_tuple[1]

    # remove all reciprocal references to the given edge (will del self-loops too)
    graph_dict[first_vertex] = [x for x in graph_dict[first_vertex] if x != second_vertex]
    graph_dict[second_vertex] = [x for x in graph_dict[second_vertex] if x != first_vertex]

    # change references in 2nd vertex's edges from 2nd vertex to 1st vertex
    for edge in graph_dict[second_vertex]:
        # an attempt to optimize this section, not sure if it worked well
        new_edge_list = list(graph_dict[edge])

        for i in range(len(new_edge_list)):
            if new_edge_list[i] == second_vertex:
                new_edge_list[i] = first_vertex

        graph_dict[edge] = new_edge_list

        # graph_dict[edge] = [x if x != second_vertex else first_vertex for x in graph_dict[edge]]

    # take edges from 2nd vertex and add to 1st vertex, del 2nd vertex
    graph_dict[first_vertex].extend(graph_dict.pop(second_vertex))

    return graph_dict


# print choose_rand_edge(graph_dict)
# print contract_edge(graph_dict, (3, 5))
# print find_min_cut(dict(graph_dict))

min_cut = len(graph_dict) - 1  # max cut possible is n-1

for i in range(50):  # running repeated trials
    # run function on a new copy of the graph each time, dictionaries are mutable
    d = dict(graph_dict)
    new_cut = find_min_cut(d)

    if new_cut < min_cut:
        min_cut = new_cut

print min_cut
