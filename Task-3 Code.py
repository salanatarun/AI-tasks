print("BFS and DFS")
from collections import deque
class GraphSearch:
    def __init__(self, graph):
        self.graph = graph

    def dfs(self, start, goal):
        stack = [(start, [start])]
        visited = set()

        while stack:
            node, path = stack.pop()
            if node not in visited:
                visited.add(node)
                if node == goal:
                    return path
                for neighbor in reversed(self.graph.get(node, [])):
                    if neighbor not in visited:
                        stack.append((neighbor, path + [neighbor]))
        return None

    def bfs(self, start, goal):
        queue = deque([(start, [start])])
        visited = set()

        while queue:
            node, path = queue.popleft()
            if node not in visited:
                visited.add(node)
                if node == goal:
                    return path
                for neighbor in self.graph.get(node, []):
                    if neighbor not in visited:
                        queue.append((neighbor, path + [neighbor]))
        return None

    def display_tree(self, start):
        visited = set()
        def dfs_tree(node, depth=0):
            if node not in visited:
                visited.add(node)
                print("  " * depth + f"|- {node}")
                for neighbor in self.graph.get(node, []):
                    dfs_tree(neighbor, depth + 1)

        print("Tree Structure:")
        dfs_tree(start)


# Example Graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

# Initial State and Goal State
initial_state = 'A'
goal_state = 'G'

search = GraphSearch(graph)

# DFS Search
dfs_path = search.dfs(initial_state, goal_state)
print("DFS Path:", dfs_path)

# BFS Search
bfs_path = search.bfs(initial_state, goal_state)
print("BFS Path:", bfs_path)

# Display Tree
search.display_tree(initial_state)
