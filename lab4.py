
def longest_path(torus):
    if not torus or len(torus) == 0 or len(torus[0]) == 0:
        return []

    m, n = len(torus), len(torus[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  

    def valid(x, y):
        return 0 <= x < m and 0 <= y < n

    def getting_neighbors(x, y):
        neighbors = []
        for dx, dy in directions:
            nx, ny = (x + dx) % m, (y + dy) % n  
            neighbors.append((nx, ny))
        return neighbors

    def dfs(x, y, path):
        path.append((x, y))
        maximum_path = []
        for nx, ny in getting_neighbors(x, y):
            if torus[nx][ny] > torus[x][y]:
                newest_path = dfs(nx, ny, path[:])  
                if len(newest_path) > len(maximum_path):
                    maximum_path = newest_path
        return maximum_path if len(maximum_path) > len(path) else path

    longest = []
    for i in range(m):
        for j in range(n):
            cpath = dfs(i, j, [])  
            if len(cpath) > len(longest):
                longest = cpath

    return longest if len(longest) >= 2 else []
