class ListofNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2,l3):
        plus_carry = 0
           if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            curr.next = ListofNode(val % 10)
            curr = curr.next
            plus_carry = int(val / 10)
        if plus_carry > 0:
            curr.next = ListofNode(plus_carry)
        return head.next
    print(l1)
    print(l2)
    print(l3)
