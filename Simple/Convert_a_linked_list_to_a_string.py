class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def stringify(node):
    if node is None:
        return "None"
    
    result = str(node.data)
    
    current = node.next
    while current is not None:
        result += " -> " + str(current.data)
        current = current.next
    
    result += " -> None"
    
    return result

node = Node(1)
node.next = Node(2)
node.next.next = Node(3)

print(stringify(node))  
print(stringify(None))  

