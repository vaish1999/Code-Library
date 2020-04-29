from collections import defaultdict 
  

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
            visited.append(node)
        remove_from_stack = True
        for next in graph[node]:
            if next not in visited:
                stack.append(next)
                step += 1
                order[next].append(step)
                remove_from_stack = False
                break
        if remove_from_stack:
            step += 1
            nd = stack.pop()
            order[nd].append(step)
    return visited, order

n, e = list(map(int, input().split()))
gph = defaultdict(list) 

for i in range(e):
    n1, n2 = list(map(int, input().split()))
    # n1, n2 = input().split()

    if n1 != n2:
        gph[n1].append(n2)
        gph[n2].append(n1)
    
# print(gph)

root = int(input())
v = int(input())

nds, order = dfs(gph, root)

rng = order[v]
rng = list(range(rng[0], rng[1] + 1))
for key in nds:
    if ((order[key][0] in rng) and (order[key][1] in rng)): 
        print(key, end = ' ')

# print(nds, order)