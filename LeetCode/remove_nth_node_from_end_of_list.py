import sys


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        fast_pointer = head
        slow_pointer = None
        counter = 0

        while(fast_pointer):
            if(counter > n):
                slow_pointer = slow_pointer.next
            if(counter == n):
                slow_pointer = head

            fast_pointer = fast_pointer.next
            counter += 1

        if(slow_pointer == None):
            return head.next

        slow_pointer.next = slow_pointer.next.next

        return head


if __name__ == "__main__":
    nums = list(map(int, input().strip().split()))
    n = int(input().strip())
    node_head = None
    prev_node = None
    for num in nums:
        new_node = ListNode(num)
        if(node_head):
            prev_node.next = new_node
        else:
            node_head = new_node
        prev_node = new_node

    node_head = Solution().removeNthFromEnd(node_head, n)
    current_node = node_head
    while(current_node):
        print(current_node.val)
        current_node = current_node.next
