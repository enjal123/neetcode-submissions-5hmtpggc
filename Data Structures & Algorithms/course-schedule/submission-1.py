class Solution:
    def canFinish(self, numCourses: int, preqR: List[List[int]]) -> bool:


        preqMap = {i: [] for i in range(numCourses)}

        for crs, preq in preqR:
            print("To take course", crs,"you need to take course", preq, "first")
            preqMap[crs].append(preq)

        visting = set()

        def dfs(crs):
            
            if crs in visting:
                return False
            if preqMap[crs] == []:
                return True

            visting.add(crs)

            for preq in preqMap[crs]:
                if dfs(preq) == False:
                    return False

            visting.remove(crs)
            preqMap[crs] = []
            return True

        for n in range(numCourses):
            if dfs(n) == False:
                return False
        
        return True


