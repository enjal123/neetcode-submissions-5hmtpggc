class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}

        for index, value in enumerate(nums):
            missing = target - value

            if missing in seen.keys():
                return [seen[missing], index]

            if value not in seen:
                seen[value] = index
        