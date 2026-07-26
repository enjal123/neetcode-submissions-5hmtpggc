class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        data = {}

        for i, x in enumerate(nums):
            
            need = target - x
            if need in data:
                return [data[need], i]

            data[x] = i