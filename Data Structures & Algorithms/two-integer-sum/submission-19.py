class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        
        n = {}
        for index, value in enumerate(nums):

           
            needed = target - value

            if needed in n:
                return [n[needed], index]
            if value not in n:
                n[value] = index
