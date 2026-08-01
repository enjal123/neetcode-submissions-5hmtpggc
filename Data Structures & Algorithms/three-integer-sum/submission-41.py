class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums = sorted(nums)

        res = []

        for curr in range(len(nums)):

            if curr > 0 and nums[curr] == nums[curr-1]:
                continue
                
            left = curr + 1
            right = len(nums) - 1

            while left < right:

                need = nums[left] + nums[right]

                if need == -nums[curr]:
                    res.append([nums[curr], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                elif need > -nums[curr]:
                    right -= 1
                else:
                    left += 1

        return res
             