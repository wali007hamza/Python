import sys


class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None

    @staticmethod
    def iterate_linked_list(head):
        curr_node = head
        while (curr_node):
            print(curr_node.val)
            curr_node = curr_node.next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if (k == 0 or head == None):
            return head
        n = self.len_linked_list(head)
        if(n == 1 or k % n == 0):
            return head
        fast_pointer = head
        for i in range(k % n):
            fast_pointer = fast_pointer.next

        slow_pointer = head
        while (fast_pointer.next):
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next

        new_head = slow_pointer.next
        slow_pointer.next = None
        fast_pointer.next = head

        return new_head

    def len_linked_list(self, head: ListNode) -> int:
        counter = 0
        curr_node = head
        while (curr_node):
            curr_node = curr_node.next
            counter += 1

        return counter


if __name__ == "__main__":
    list_of_numbers = input().strip().split("->")
    k = int(input().strip())
    head_node = ListNode(list_of_numbers[0])
    prev_node = head_node
    for number in list_of_numbers[1:len(list_of_numbers) - 1]:
        curr_node = ListNode(number)
        prev_node.next = curr_node
        prev_node = curr_node

    new_head = Solution().rotateRight(head_node, k)
    ListNode.iterate_linked_list(new_head)
