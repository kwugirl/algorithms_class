from sys import argv

script, filename = argv

txt = open(filename)

# run through file to get out all the numbers in the list
# each line looks like "1\t2\t3\t\n"
graph_fwd = {}
graph_rvs = {}
max_node = 0
for line in txt:
    line = line.rstrip().split(' ')  # strip off trailing whitespaces, split at spaces
    for i in range(len(line)):
        line[i] = int(line[i])

    if line[0] > max_node:
        max_node = line[0]

    graph_fwd.setdefault(line[0],[]).append(line[1])
    graph_rvs.setdefault(line[1],[]).append(line[0])

txt.close()

# print graph_fwd
# print graph_rvs
graph_fwd_explored = {}
graph_rvs_explored = {}
finishing_times = []
scc_sizes = []


def dfs(graph, node, explored, direction):
    stack = [node]
    size = 1

    while len(stack) > 0:
        last = stack[-1]

        new_nodes = False

        if last in graph:
            child_nodes = graph[last]

            for node in child_nodes:
                if node not in explored:
                    explored[node] = "explored"
                    stack.append(node)
                    size += 1
                    new_nodes = True

        if new_nodes is False:
            last = stack.pop(-1)

            if direction == "rvs":
                finishing_times.append(last)

    if direction == "fwd":
        scc_sizes.append(size)

# explore reverse graph
for i in range(max_node, 0, -1):
    if i not in graph_rvs_explored:
        graph_rvs_explored[i] = "explored"
        dfs(graph_rvs, i, graph_rvs_explored, direction = "rvs")

# print finishing_times

# explore forward graph
for i in range(1, len(finishing_times)+1):
    node = finishing_times[-i]

    if node not in graph_fwd_explored:
        graph_fwd_explored[node] = "explored"
        dfs(graph_fwd, node, graph_fwd_explored, direction = "fwd")

scc_sizes.sort(reverse = True)

if len(scc_sizes) > 5:
    print scc_sizes[:5]
else:
    print scc_sizes
