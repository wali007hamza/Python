import sys
import ListNode


class Solution():
    def swapPairs(self, head):
        prev_node = None
        pointer = head
        node1 = None
        node2 = None
        head_node = None

        while(pointer):
            next_node = None
            node1 = pointer
            node2 = pointer.next
            if(node2):
                next_node = node2.next
            else:
                node2 = node1
                node1 = None
            if(prev_node):
                prev_node.next = node2
            else:
                head_node = node2
            node2.next = node1
            if(node1):
                node1.next = next_node
            pointer = next_node
            prev_node = node1

        return head_node


if __name__ == "__main__":
    nums = list(map(int, input().strip().split()))

    head_node = None
    prev_node = None

    for num in nums:
        new_node = ListNode.ListNode(num)
        if(not(head_node)):
            head_node = new_node
        else:
            prev_node.next = new_node
        prev_node = new_node

    ret_head_node = Solution().swapPairs(head_node)
    ListNode.TraverseList(ret_head_node)
