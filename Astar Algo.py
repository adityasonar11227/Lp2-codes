import heapq

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(grid, start, goal):
    open_set = [(heuristic(start, goal), 0, start)]
    came_from, g_score = {}, {start: 0}
    rows, cols = len(grid), len(grid[0])

    while open_set:
        _, cost, current = heapq.heappop(open_set)

        if current == goal:
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            return path[::-1]

        x, y = current
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x + dx, y + dy
            neighbor = (nx, ny)
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
                new_cost = cost + 1
                if neighbor not in g_score or new_cost < g_score[neighbor]:
                    g_score[neighbor] = new_cost
                    heapq.heappush(open_set, (new_cost + heuristic(neighbor, goal), new_cost, neighbor))
                    came_from[neighbor] = current
    return None

# Example usage
grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]

start, goal = (0, 0), (4, 4)
path = astar(grid, start, goal)

print("Path found:" if path else "No path found.")
if path:
    for step in path:
        print(step)
