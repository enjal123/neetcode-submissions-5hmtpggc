class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums = sorted(nums)
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
                    right -=1
                    while left< right and nums[left] == nums[left-1]:
                        left +=1 
                if need > -nums[curr]:
                    right -= 1
                    continue
                if need < -nums[curr]:
                    left +=1

        return res

             