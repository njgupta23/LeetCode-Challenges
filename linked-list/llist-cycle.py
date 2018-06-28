# Linked List Cycle

# Given a linked list, determine if it has a cycle in it.

# Follow up:
# Can you solve it without using extra space?


def hasCycle(head):

    fast = head
    slow = head
    
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        
        if fast == slow:
            return True
        
    return False
