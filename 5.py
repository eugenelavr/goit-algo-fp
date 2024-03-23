import uuid
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def init(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_edges_with_positions(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        pos[node.id] = (x, y)

        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 
            layer
            pos[node.left.id] = (l, y - 1)
            add_edges_with_positions(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)

        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 
            layer
            pos[node.right.id] = (r, y - 1)
            add_edges_with_positions(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)

    return graph, pos

def dfs(node, visited=None, color_map=None, colors=None):
    if visited is None:
        visited = []
    if color_map is None:
        color_map = {}
    if colors is None:
        colors = ['#000000']  # початковий колір

    if node:
        visited.append(node)
        color_map[node.id] = colors[-1]  # присвоєння кольору вузлу
        next_color = '#{:02x}{:02x}{:02x}'.format(min(int(colors[-1][1:3], 16) + 20, 255),
                                                  min(int(colors[-1][3:5], 16) + 20, 255),
                                                  min(int(colors[-1][5:7], 16) + 20, 255))
        colors.append(next_color)

        dfs(node.left, visited, color_map, colors)
        dfs(node.right, visited, color_map, colors)

    return visited, color_map

def bfs(root):
    visited, queue = [], [root]
    color_map = {}
    colors = ['#000000']  # початковий колір
    while queue:
        node = queue.pop(0)
        if node and node not in visited:
            visited.append(node)
            color_map[node.id] = colors[-1]
            next_color = '#{:02x}{:02x}{:02x}'.format(min(int(colors[-1][1:3], 16) + 20, 255),
                                                      min(int(colors[-1][3:5], 16) + 20, 255),
                                                      min(int(colors[-1][5:7], 16) + 20, 255))
            colors.append(next_color)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return visited, color_map

def draw_tree_with_traversal(root, traversal_type='dfs'):
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

# Створення бінарного дерева для демонстрації обходу
root = Node(0)
root.left = Node(1)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.left = Node(5)

# Візуалізація обходу дерева
draw_tree_with_traversal(root, 'dfs')
draw_tree_with_traversal(root, 'bfs')