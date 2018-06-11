# Delete Node in a Linked List

# Write a function to delete a node (except the tail)
# in a singly linked list, given only access to that node.

# example:
# 4 -> 5 -> 1 -> 9, node = 5
# >> 4 -> 1 -> 9

# Note:

# The linked list will have at least two elements.
# All of the nodes' values will be unique.
# The given node will not be the tail and it will always be a valid node of the linked list.
# Do not return anything from your function.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def deleteNode(node):
    node.val = node.next.val
    node.next = node.next.next
