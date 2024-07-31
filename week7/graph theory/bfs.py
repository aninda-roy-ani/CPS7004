from collections import deque

tree = {
    '0': '1',
    '1': '3',
    '2': '1',
    '3': ('2', '4'),
    '4': ('6', '5'),
    '5': '7',
    #'6': '4',
    #'7': '6'
}

def bfs(tree, start):

    q = deque([start])
    visited = []
    traversal_order = []

    while q:

        node = q.popleft()
        if node not in visited:
            visited.append(node)
            traversal_order.append(node)
            if node in tree:
                children = tree[node]
                if isinstance(children, tuple):
                    children = list(children)
                for child in children:
                    if child not in visited:
                        q.append(child)
    return traversal_order


print(bfs(tree, '0'))