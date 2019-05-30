import sys
from ListNode import ListNode, TraverseList


class Solution:
    def reverseKGroup(self, head, k):
        curr_pos = 0
        curr_node = head
        while(curr_node):
            for i in range(0, k):
                if(curr_node):
                    curr_node = curr_node.next
            new_head = reverse_linked_list(head, curr_pos, curr_pos + k - 1)
            curr_pos += k

        return new_head


def reverse_linked_list(head, from_pos, to_pos):
    print(from_pos, ' ', to_pos)
    curr_pos = 0
    prev_node = None
    curr_node = head
    start_node = None
    while(curr_pos < from_pos):
        curr_pos += 1
        start_node = curr_node
        curr_node = curr_node.next

    reversal_head = curr_node
    while(curr_pos >= from_pos and curr_pos <= to_pos and curr_node):
        next_node = curr_node.next
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = next_node
        curr_pos += 1

    reversal_head.next = curr_node
    if(start_node):
        start_node.next = prev_node

        return head
    else:
        return prev_node


if __name__ == "__main__":
    nums = list(map(int, input().strip().split()))
    k = int(input().strip())
    head_node = None
    prev_node = None
    for num in nums:
        new_node = ListNode(num)
        if(head_node):
            prev_node.next = new_node
        else:
            head_node = new_node
        prev_node = new_node

    ret_head_node = Solution().reverseKGroup(head_node, k)
    TraverseList(ret_head_node)
