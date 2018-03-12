class AddTwoNumbers:

    def addTwoNumbers(self, l1, l2):
        pointer1 = l1
        pointer2 = l2
        result_list = None

        carry = 0
        prev_pointer = None
        while(pointer1 != None or pointer2 != None or carry != 0):
            addend1 = 0
            addend2 = 0
            if(pointer1 != None):
                addend1 = pointer1.val
                pointer1 = pointer1.next

            if(pointer2 != None):
                addend2 = pointer2.val
                pointer2 = pointer2.next

            summation = carry + addend1 + addend2
            carry = int(summation / 10)
            new_node = ListNode(summation % 10)
            if(result_list == None):
                result_list = new_node
            else:
                prev_pointer.next = new_node

            prev_pointer = new_node

        return result_list


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    @staticmethod
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
