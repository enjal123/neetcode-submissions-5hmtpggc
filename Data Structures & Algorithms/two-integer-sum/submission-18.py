class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        data = {}
    
        for index, value in enumerate(nums):
            
         
            needed = target - value
       
            if needed in data:
                return [data[needed], index]

            if value not in data:
                data[value] = index
            else:
                continue
