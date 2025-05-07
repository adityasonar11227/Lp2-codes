import heapq

def prim_mst(graph):
    n = len(graph)
    visited = [False] * n
    min_heap = [(0, 0)]  # (weight, node)
    total_weight = 0
    mst_edges = []

    while min_heap:
        weight, u = heapq.heappop(min_heap)
        if visited[u]:
            continue

        visited[u] = True
        total_weight += weight

        for v, w in graph[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (w, v))
                mst_edges.append((u, v, w))

    return total_weight, mst_edges

# Example graph with 5 nodes
graph = {
    0: [(1, 2), (3, 6)],
    1: [(0, 2), (2, 3), (3, 8), (4, 5)],
    2: [(1, 3), (4, 7)],
    3: [(0, 6), (1, 8)],
    4: [(1, 5), (2, 7)]
}

graph_list = [[] for _ in range(5)]
for u in graph:
    for v, w in graph[u]:
        graph_list[u].append((v, w))

total_weight, mst_edges = prim_mst(graph_list)

print("Total weight of MST:", total_weight)
print("Edges in MST:")
for u, v, w in mst_edges:
    print(f"{u} - {v} (weight: {w})")
