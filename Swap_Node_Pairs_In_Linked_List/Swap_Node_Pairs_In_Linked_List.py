class Node:
    def __init__(self, next=None):
        self.next = next

def swap_pairs(head):
    dummy = Node()
    dummy.next = head
    prev = dummy

    while head and head.next:
        first = head
        second = head.next

        prev.next = second
        first.next = second.next
        second.next = first

        prev = first
        head = first.next

    return dummy.next
