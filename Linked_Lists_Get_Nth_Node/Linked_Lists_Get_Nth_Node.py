class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def get_nth(node, index):
    if node is None:
        raise Exception("List is empty")
    if index < 0:
        raise Exception("Index cannot be negative")
    
    current = node
    count = 0
    
    while current is not None:
        if count == index:
            return current
        count += 1
        current = current.next
    
    raise Exception("Index out of range")