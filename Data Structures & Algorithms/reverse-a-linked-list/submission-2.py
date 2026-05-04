
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None
        curr = head #node A ---> Node b

        while curr:
            next_node = curr.next #next node so next_node = B
            curr.next = prev
            prev = curr # now node None = A 
            curr = next_node

        return prev
            
