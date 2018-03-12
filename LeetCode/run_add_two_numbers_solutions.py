import sys
from AddTwoNumbersSolution import ListNode
from AddTwoNumbersSolution import AddTwoNumbers


def createListNodes(num: int):
    head = None
    prev_pointer = None

    while(num > 0):
        val = num % 10
        num = int(num / 10)
        node = ListNode(val)
        if(head == None):
            head = node
        else:
            prev_pointer.next = node

        prev_pointer = node

    return head


if __name__ == "__main__":
    num1, num2 = tuple(map(int, input().strip().split()))
    list1 = createListNodes(num1)
    list2 = createListNodes(num2)

    return_list = AddTwoNumbers().addTwoNumbers(list1, list2)
    pointer = return_list
    while(pointer != None):
        print(pointer.val)
        pointer = pointer.next
