# Reverse Linked List

# Example:

# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL


def reverseList(head):
        
    curr = head
    prev = None
    
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    
    head = prev
    
    return head
