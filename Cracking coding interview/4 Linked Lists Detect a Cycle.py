
'''

https://www.geeksforgeeks.org/detect-and-remove-loop-in-a-linked-list/


https://www.geeksforgeeks.org/detect-loop-in-a-linked-list/
http://blog.ostermiller.org/find-loop-singly-linked-list

https://www.geeksforgeeks.org/how-does-floyds-slow-and-fast-pointers-approach-work/
'''


class Node:
  
    def __init__(self, data):
        self.data = data
        self.next = None
  
class LinkedList:
  
    # Function to initialize head
    def __init__(self):
        self.head = None
  

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
  

    def printList(self):
        temp = self.head
        while(temp):
            print (temp.data,end=" ")
            temp = temp.next
  
  
    def detectLoop(self):
         s = set()
         temp=self.head
         while (temp):
         

            if (temp in s):
                return True
    
            s.add(temp)
    
            temp = temp.next

         return False
  
# Driver program for testing
llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(10)
  
# Create a loop for testing
llist.head.next.next.next.next = llist.head;
 
if( llist.detectLoop()):
    print ("Loop found")
else :
    print ("No Loop ")

"""

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


def has_cycle(head):
    slow = head
    fast = head

    while fast != None:
        slow = slow.next

        if fast.next != None:
            fast = fast.next.next
        else:
            return False

        if slow is fast:
            return True
    return False


"""



'''
# Node class
class Node:
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    # Function to initialize head
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Utility function to prit the linked LinkedList
    def printList(self):
        temp = self.head
        while (temp):
            print
            temp.data,
            temp = temp.next

    def detectLoop(self):
        slow_p = self.head
        fast_p = self.head
        while (slow_p and fast_p and fast_p.next):
            slow_p = slow_p.next
            fast_p = fast_p.next.next
            if slow_p == fast_p:
                print("Found Loop")
                return


# Driver program for testing
llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(10)

# Create a loop for testing
llist.head.next.next.next.next = llist.head
llist.detectLoop()

'''
