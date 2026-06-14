class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}

        for index, value in enumerate(nums):

            missing = target - value

            if missing in seen:
                return [seen[missing], index]

            seen[value] = index