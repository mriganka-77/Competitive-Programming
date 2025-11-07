# Only define ListNode if it's not already provided by the judge.
try:
    ListNode  # check if name exists
except NameError:
    class ListNode(object):
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        Add two numbers represented by reversed linked lists.
        Returns the head ListNode of the resulting linked list.
        """
        dummy = ListNode(0)
        cur = dummy
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            s = v1 + v2 + carry
            carry = s // 10
            cur.next = ListNode(s % 10)
            cur = cur.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next

# Optional: helper functions for local testing. Safe to leave in file.
def list_to_linked(arr):
    dummy = ListNode(0)
    cur = dummy
    for x in arr:
        cur.next = ListNode(x)
        cur = cur.next
    return dummy.next

def linked_to_list(node):
    out = []
    while node:
        out.append(node.val)
        node = node.next
    return out

if __name__ == "__main__":
    # Quick local sanity checks
    s = Solution()
    print(linked_to_list(s.addTwoNumbers(list_to_linked([2,4,3]), list_to_linked([5,6,4]))))  # [7,0,8]
    print(linked_to_list(s.addTwoNumbers(list_to_linked([0]), list_to_linked([0]))))        # [0]
    print(linked_to_list(s.addTwoNumbers(list_to_linked([9,9,9,9,9,9,9]),
                                         list_to_linked([9,9,9,9]))))                      # [8,9,9,9,0,0,0,1]
