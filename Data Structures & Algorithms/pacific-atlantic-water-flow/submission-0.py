class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        rows = len(heights)
        cols = len(heights[0])

        pacific = set()
        atlantic = set()

        def dfs(r, c, visted, pre_height):
            if (r < 0 or c < 0 or 
                r >= rows or c >= cols or 
                (r, c) in visted or 
                heights[r][c] < pre_height):
                return
            
            visted.add((r, c))
            
            dfs(r + 1, c, visted, heights[r][c])
            dfs(r - 1, c, visted, heights[r][c])
            dfs(r, c + 1, visted, heights[r][c])
            dfs(r, c - 1, visted, heights[r][c])

        # Kick off DFS from Top and Bottom borders
        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])
            dfs(rows - 1, c, atlantic, heights[rows - 1][c])

        # Kick off DFS from Left and Right borders
        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, cols - 1, atlantic, heights[r][cols - 1])

        # Collect cells that can reach both oceans
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])

        return res