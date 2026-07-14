class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        key = {i: [] for i in range(n)}

        for start, go in edges:
            key[start].append(go)
            key[go].append(start)

        visited = set()
        components = 0 

        def dfs(node):

            if node in visited:
                return 

            visited.add(node)
            if node not in visited:
                dfs(node)
                components += 1

            for neighbor in key[node]:
                dfs(neighbor)
        
        for n in range(n):
            if n not in visited:
                dfs(n)
                components += 1
        return components


        