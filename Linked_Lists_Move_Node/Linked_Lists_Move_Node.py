class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest
    
def move_node(source, dest):
    if source is None:
        raise Exception("Source list is empty")
    
    node_to_move = source
    source = source.next
    node_to_move.next = dest
    dest = node_to_move
    
    return Context(source, dest)