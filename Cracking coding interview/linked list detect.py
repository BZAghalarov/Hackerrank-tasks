
class Node(object):
    def __init__(self, value, next=None):
        self.next=next
        self.value=value
def create_list():
    last = Node(8)
    head = Node(7, last)
    head = Node(6, head)
    head = Node(5, head)
    head = Node(4, head)
    head = Node(3, head)
    head = Node(2, head)
    head = Node(1, head)
    last.next = head
    return head

def is_circular(head):
    slow = head
    fast = head
    while True:
        slow = slow.next
        print(slow)
        fast = fast.next.next
        print(fast)
        print (slow.value, fast.value)
        if slow.value == fast.value:
            return True
        elif slow is fast:
            return False

node = create_list()
print (is_circular(node))