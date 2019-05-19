import sys


class Node:
    def __init__(self, val: int, prev_node=None):
        self.val = val
        if (prev_node):
            prev_node.next = self
        self.next = None
        self.prev = None

    @staticmethod
    def forward_traverse(start_node):
        traversal_list = list()
        curr_node = start_node
        prev_node = None
        while(curr_node):
            traversal_list.append(curr_node.val)
            prev_node = curr_node
            curr_node = curr_node.next

        print(traversal_list)
        return prev_node

    @staticmethod
    def reverse_traverse(end_node):
        traversal_list = list()
        curr_node = end_node
        while(curr_node):
            traversal_list.append(curr_node.val)
            curr_node = curr_node.prev

        print(traversal_list)


if __name__ == "__main__":
    if (len(sys.argv) < 1 or len(sys.argv) > 3):
        raise Exception("Invalid arguments")
    array = list(map(int, sys.argv[1].split(',')))
    node_head = Node(array[0])
    prev_node = node_head
    for num in array[1:]:
        curr_node = Node(num, prev_node)
        curr_node.prev = prev_node
        prev_node = curr_node
    if(str(sys.argv[2]) == "forward"):
        Node.forward_traverse(node_head)
    if(str(sys.argv[2]) == "reverse"):
        last_node = Node.forward_traverse(node_head)
        Node.reverse_traverse(last_node)
