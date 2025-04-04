class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    if head is None or head.next is None:
        raise ValueError("List must contain at least two nodes")

    first_dummy = Node()
    second_dummy = Node()
    first_tail = first_dummy
    second_tail = second_dummy

    current = head
    toggle = True

    while current:
        if toggle:
            first_tail.next = current
            first_tail = first_tail.next
        else:
            second_tail.next = current
            second_tail = second_tail.next
        current = current.next
        toggle = not toggle

    first_tail.next = None
    second_tail.next = None

    return Context(first_dummy.next, second_dummy.next)
