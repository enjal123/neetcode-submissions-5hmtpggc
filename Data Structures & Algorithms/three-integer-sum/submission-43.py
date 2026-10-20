class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        
        right = len(nums) -1
        left = 0

        count = {}
        for index, value in enumerate(nums):
            if value not in count:
                count[value] = index
            else:
                continue

        res = set()
        for i in range(len(nums)):
            triplet = []
            for j in range(len(nums)):
                needed = -nums[i] - nums[j]
                if needed in count and count[needed] != i and count[needed] != j and i != j:
                    triplet = [nums[i], nums[j], nums[count[needed]]]
                    res.add(tuple(sorted(triplet)))
                    continue

        return list(res)
