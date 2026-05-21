class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(start, total, path):
            if total == target:
                res.append(path[:])
                return
            if total > target:
                return
            
            for i in range(start, len(nums)):
                num = nums[i]

                path.append(num)

                backtrack(i, total + num, path)

                path.pop()

        
        backtrack(0, 0, [])

        return res