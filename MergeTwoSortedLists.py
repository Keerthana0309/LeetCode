#Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.
#Example:
#Input: 1->2->4, 1->3->4
#Output: 1->1->2->3->4->4


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        
        dummy = ListNode()
        cur = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                #add the smaller one into new node list
                cur.next = ListNode(l1.val)
                #l1 move forward
                l1 = l1.next
            else:
                #add the smaller one into new node list
                cur.next = ListNode(l2.val)
                #l2 move forward
                l2 = l2.next
                
            #move the new node list forward
            cur = cur.next
                        
            
        if l1:
            cur.next = l1
        if l2:
            cur.next = l2
            
        return dummy.next    
