
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __eq__(self, other):
        if isinstance(other, ListNode):
            return self.val == other.val
        return False


class Node:
    def __init__(self, l):
        self.raw = l
        self.head = self.get_node()

    def get_head(self):
        return self.head

    def get_node(self):
        a = self.raw
        headA = ListNode(a[0])
        temp = headA
        for i, val in enumerate(a):
            if i == 0:
                continue
            else:
                temp.next = ListNode(a[i])
                temp = temp.next
        return headA

    def __repr__(self):
        a = map(str, self.raw)
        return " -> ".join(a)

if __name__ == '__main__':
    test = [1, 2, 3, 4, 5]
    node = Node(test)
    head = node.get_head()
    tmp = head
    while tmp:
        print(tmp.val, end="->")
        tmp = tmp.next