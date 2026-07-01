class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        data = {}

        for index, value in enumerate(nums):
            needed = target - value # 92 - 95 = -3

            if needed in data.keys(): 
                return [data[needed], index]

            if value not in data: 
                data[value] = index # 4: 0 , 5: 1
            else:
                continue
            
            
