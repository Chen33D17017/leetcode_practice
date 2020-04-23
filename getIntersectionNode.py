from tool import Node
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None
        else:
            pA, pB = headA, headB
            while pA != pB:
                pA = pA.next if pA else headB
                pB = pB.next if pB else headA
            return pA



if __name__ == '__main__':
    pass