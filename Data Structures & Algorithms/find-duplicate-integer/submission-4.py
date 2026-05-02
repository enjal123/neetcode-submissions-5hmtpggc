class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        seen = set()

        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                return num
