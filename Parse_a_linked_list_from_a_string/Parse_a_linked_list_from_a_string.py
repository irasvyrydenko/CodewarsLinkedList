from preloaded import Node
def linked_list_from_string(s):
    if s == "None":
        return None
    values = s.split(" -> ")
    if values[-1] == "None":
        values.pop()
    if not values:
        return None
    head = Node(int(values[0]))
    current = head
    for value in values[1:]:
        current.next = Node(int(value))
        current = current.next
    return head