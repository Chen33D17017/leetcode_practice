class FirstUnique(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.dict = {}
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next, self.tail.prev = self.tail, self.head

        for num in nums:
            self.add(num)

    def insertNode(self, val):
        last_prev_node = self.tail.prev
        new_node = Node(val)
        last_prev_node.next, new_node.prev = new_node, last_prev_node
        new_node.next, self.tail.prev = self.tail, new_node
        return new_node

    def deleteNode(self, node):
        prev_node = node.prev
        prev_node.next, node.next.prev = node.next, prev_node

    def showFirstUnique(self):
        """
        :rtype: int
        """
        if self.head.next == self.tail:
            return -1
        else:
            return self.head.next.val

    def add(self, value):
        """
        :type value: int
        :rtype: None
        """
        if value not in self.dict:
            self.dict[value] = self.insertNode(value)
        elif not self.dict[value]:
            return
        else:
            self.deleteNode(self.dict[value])
            self.dict[value] = None


class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

def main():
    firstUnique = FirstUnique([7, 7, 7, 7, 7])
    print(firstUnique.showFirstUnique())
    firstUnique.add(7)
    firstUnique.add(3)
    firstUnique.add(3)
    firstUnique.add(7)
    firstUnique.add(17)
    print(firstUnique.showFirstUnique())


if __name__ == '__main__':
    main()

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)