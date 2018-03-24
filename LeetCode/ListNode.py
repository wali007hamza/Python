class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def TraverseList(head_node : ListNode):
    current_node = head_node
    while(current_node):
        print(current_node.val)
        current_node = current_node.next