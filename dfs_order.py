def dfs(graph, node):
    
    order ={ k:[] for k in graph.keys()}
    # print(order)
    step = 0

    visited = [node]
    stack = [node]
    step += 1
    order[node].append(step)

    while stack:
        node = stack[-1]
        if node not in visited:
            visited.extend(node)
        remove_from_stack = True
        for next in graph[node]:
            if next not in visited:
                stack.extend(next)
                step += 1
                order[next].append(step)
                remove_from_stack = False
                break
        if remove_from_stack:
            step += 1
            nd = stack.pop()
            order[nd].append(step)
    return visited, order


# graph1 = {
#     'A' : ['B','S'],
#     'B' : ['A'],
#     'C' : ['D','E','F','S'],
#     'D' : ['C'],
#     'E' : ['C','H'],
#     'F' : ['C','G'],
#     'G' : ['F','S'],
#     'H' : ['E','G'],
#     'S' : ['A','C','G']
# }


graph1 = {
    'a' : ['b','c', 'd'],
    'b' : ['a','c'],
    'c' : ['a', 'b', 'd'],
    'd' : ['a', 'c']
}


print (dfs(graph1, 'a'))