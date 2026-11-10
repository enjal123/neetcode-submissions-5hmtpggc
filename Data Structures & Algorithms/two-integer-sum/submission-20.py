class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        n = {}

        for index, value in enumerate(nums):
            needed = target-value

            if needed in n.keys():
                return [n[needed], index]
            
            n[value] = index

        
        return []

