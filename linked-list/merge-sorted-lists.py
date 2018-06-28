# Merge Two Sorted Lists

# Merge two sorted linked lists and return it as a new list. 
# The new list should be made by splicing together the nodes 
# of the first two lists.

# Example:

# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4


def mergeTwoLists(self, l1, l2):
    if not l1:
        return l2
    if not l2:
        return l1
    
    first = False

    if l1.val < l2.val:
        curr = l1
        other = l2
        first = True
    else:
        curr = l2
        other = l1
    
    while curr:
        if curr.next is None:
            curr.next = other
            if first is True:
                return l1
            else:
                return l2
        
        elif curr.next.val >= other.val:
            save = curr.next
            curr.next = other
            other = save
        
        curr = curr.next
