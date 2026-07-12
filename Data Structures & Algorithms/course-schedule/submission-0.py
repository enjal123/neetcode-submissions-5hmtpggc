class Solution:
    def canFinish(self, numCourses: int, preqR: List[List[int]]) -> bool:
        

        preMap = {i: [] for i in range(numCourses)}

        for crs, preq in preqR:
            preMap[crs].append(preq)

        visting = set()

        def dfs(crs):

            if crs in visting:
                return False
            if preMap[crs] == []:
                return True

            visting.add(crs)

            for pre in preMap[crs]:
                if dfs(pre) == False:
                    return False
            
            visting.remove(crs)
            preMap[crs] = []

            return True


        for c in range(numCourses):
            if not dfs(c):
                return False
            
        return True
