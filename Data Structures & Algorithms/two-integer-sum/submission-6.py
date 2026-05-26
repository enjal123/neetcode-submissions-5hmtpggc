class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        compliments = {}

        for n in range(len(nums)):
            needed = target - nums[n]

            if needed in compliments:
                return [compliments[needed], n]
            
            compliments[nums[n]] = n