# URL: https://leetcode.com/problems/add-two-numbers/
# Time complexity: O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        # Create a result node to return the resulting linked list
        res = ListNode(0)
        current = res

        # We initialize a variable carry with the value zero to represent the carry (excess value) during the addition. The carry is the value when the sum of the digits is greater than 9.
        carry = 0
    
        # Traverse both lists while there were nodes in at least one of them
        while l1 or l2:

            # Get the value of each node or 0 if the list is linked to lower
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
        
            # Calculate sum of node values and carry value (if any)
            total = carry + x + y
            carry = total // 10 # Calculate the carry value
            current.next = ListNode(total % 10) # Create a new node with the correct digit
            current = current.next
        
            # Move to the next node in both additional lists, if any
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        # Check if there is still carry after going through all administrative lists
        if carry > 0:
            current.next = ListNode(carry)
    
        # Returns the resulting linked list, ignoring the initial result node
        return res.next
