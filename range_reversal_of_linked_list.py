import sys


class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None


def construct_linked_list(values: list):
    head = None
    prev = None
    for val in values:
        node = Node(val)
        if(head == None):
            head = node
            prev = node
            continue

        prev.next = node
        prev = node

    return head


def print_linked_list(head: Node):
    node = head
    values = list()
    while(node != None):
        values.append(node.val)
        node = node.next

    print(values, ' ')


def attempt_reverse(start_node: Node, pos_node: Node, stop_node: Node):
    if(pos_node == stop_node):
        return None
    current_node = pos_node
    returned_node = attempt_reverse(start_node, current_node.next, stop_node)
    # print(returned_node.val if returned_node != None else None)
    if(returned_node != None):
        returned_node.next = current_node
    else:
        start_node.next = current_node

    return current_node


def reverse_linked_list(start_pos: int, end_pos: int, linked_list: Node):
    index = 0
    node_start = None
    node_end = None
    current_node = linked_list
    while(index + 1 < start_pos):
        current_node = current_node.next
        index += 1
    node_start = current_node
    while((index < end_pos + 1) and current_node != None):
        current_node = current_node.next
        index += 1
    node_end = current_node

    reversed_head = attempt_reverse(node_start, node_start.next, node_end)
    reversed_head.next = node_end


if __name__ == "__main__":
    values = list(map(int, input().strip().split()))
    start_pos, end_pos = map(int, input().strip().split())
    head = construct_linked_list(values)
    reverse_linked_list(start_pos, end_pos, head)
    print_linked_list(head)
