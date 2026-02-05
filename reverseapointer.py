
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverse_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next  # Now this works because 'current' is a Node
        current.next = prev
        prev = current
        current = next_node
    return prev


def create_linked_list(arr):
    if not arr: return None
    head = Node(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = Node(val)
        curr = curr.next
    return head

def print_list(head):
    elements = []
    while head:
        elements.append(str(head.data))
        head = head.next
    print(" -> ".join(elements))


normal_list = [1, 2, 3, 4, 5]
# Convert the array to a Linked List first
linked_head = create_linked_list(normal_list)

# Reverse it
reversed_head = reverse_list(linked_head)

# Output the result
print("The reversed list is:")
print_list(reversed_head)
