class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        pairs = {i: [] for i in range(n)}

        for start, go in edges:
            print(start,"-->", go)
            pairs[start].append(go)
            pairs[go].append(start)
        
        
        visited = set()

        def dfs(start, parent):

            if start in visited:
                return False
            if start == []:
                return True

            visited.add(start)
            
            for go in pairs[start]:
                if go == parent:
                    continue
                if dfs(go, start) == False:
                    return False

            pairs[start] = []
            return True

        if not dfs(0,-1):
            return False

        if len(visited) == n:
            return True
        
        return False
            