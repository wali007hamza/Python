import sys
from ListNode import ListNode, TraverseList

class Solution():
    def mergeTwoLists(self, l1, l2):
        pointer1 = l1
        pointer2 = l2
        new_list_head = None
        new_list_prev = None
        while(pointer1 and pointer2):
            val = 0
            if(pointer1.val < pointer2.val):
                val = pointer1.val
                pointer1 = pointer1.next
            else:
                val = pointer2.val
                pointer2 = pointer2.next
            new_node = ListNode(val)
            if(not(new_list_head)):
                new_list_head = new_node
            else:
                new_list_prev.next = new_node

            new_list_prev = new_node

        if(not(new_list_head)):
            new_list_head = pointer1 if(pointer1) else pointer2
            return new_list_head

        new_list_prev.next = pointer1 if(pointer1) else pointer2
        return new_list_head


if __name__ == "__main__":
    list1 = list(map(int, input().strip().split()))
    list2 = list(map(int, input().strip().split()))
    head_node1 = None
    prev_node = None
    for num in list1:
        new_node = ListNode(num)
        if(not(head_node1)):
            head_node1 = new_node;
        else:
            prev_node.next = new_node
        prev_node = new_node

    head_node2 = None
    for num in list2:
        new_node = ListNode(num)
        if(not(head_node2)):
            head_node2 = new_node;
        else:
            prev_node.next = new_node
        prev_node = new_node


    head_node = Solution().mergeTwoLists(head_node1, head_node2)
    TraverseList(head_node)
