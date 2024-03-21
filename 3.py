import heapq

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for i in range(vertices)]

    def add_edge(self, u, v, weight):
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))

    def dijkstra(self, src):
        min_heap = [(0, src)]
        distances = [float('inf')] * self.V
        distances[src] = 0

        while min_heap:
            dist, u = heapq.heappop(min_heap)

            # Якщо відстань, що вилучається, більша за поточну відстань у масиві, продовжуємо
            if dist > distances[u]:
                continue

            for neighbor, weight in self.graph[u]:
                if distances[u] + weight < distances[neighbor]:
                    distances[neighbor] = distances[u] + weight
                    heapq.heappush(min_heap, (distances[neighbor], neighbor))

        return distances

# Створення графа для тестування
g = Graph(5)
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 3)
g.add_edge(1, 2, 1)
g.add_edge(1, 3, 2)
g.add_edge(2, 1, 4)
g.add_edge(2, 3, 8)
g.add_edge(2, 4, 2)
g.add_edge(3, 4, 7)
g.add_edge(4, 3, 9)

# Запуск алгоритму Дейкстри
src = 0  # початкова вершина
distances = g.dijkstra(src)
distances
