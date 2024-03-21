def add_edges_with_positions(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        pos[node.id] = (x, y)

        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges_with_positions(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)

        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges_with_positions(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)

    return graph, pos

def draw_tree_with_traversal_updated(root, traversal_type='dfs'):
    if traversal_type == 'dfs':
        _, color_map = dfs(root)
    else:
        _, color_map = bfs(root)

    tree = nx.DiGraph()
    tree, pos = add_edges_with_positions(tree, root, {}, 0, 0)

    colors = [color_map[node[0]] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(10, 6))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.title(f"{traversal_type.upper()} Traversal Visualization")
    plt.show()

# Повторна візуалізація обходу дерева в глибину (DFS) та в ширину (BFS)
draw_tree_with_traversal_updated(root, 'dfs')
draw_tree_with_traversal_updated(root, 'bfs')
