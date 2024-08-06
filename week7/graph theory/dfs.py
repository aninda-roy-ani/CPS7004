
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


def dfs(tree, start):

    q = [start]
    visited = []
    traversal_order = []

    while q:

        node = q.pop()
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


print(dfs(tree, '0'))