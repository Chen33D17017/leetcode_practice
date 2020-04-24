# LRUCache cache = new LRUCache( 2 /* capacity */ );
#
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.put(4, 4);    // evicts key 1
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.len = 0
        self.cap = capacity
        self.cache = {}
        self.first = DoubleLinkNode(0)
        self.last = DoubleLinkNode(0)
        self.first.next = self.last
        self.last.prev = self.first

    def __repr__(self):
        if self.first.next == self.last:
            return "-1"
        rst = ""
        node = self.first.next
        while node != self.last :
            rst += f"{node.val}->"
            node = node.next
        rst += "\n"
        rst += "reverse:\n"
        node = self.last.prev
        while node != self.first:
            rst += f"{node.val}->"
            node = node.prev
        return rst


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1
        if not self.cache[key].val:
            del(self.cache[key])
            return -1
        else:
            prev_node = self.cache[key].prev
            prev_node.next, self.cache[key].next.prev = self.cache[key].next, prev_node
            second_node = self.first.next
            second_node.prev, self.cache[key].next = self.cache[key], second_node
            self.first.next, self.cache[key].prev = self.cache[key], self.first
            return self.cache[key].val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if self.get(key) != -1:
          self.cache[key].val = value
          return
        elif self.len < self.cap :
            # Assign new node
            self.len += 1
        else:
            del_node = self.last.prev
            # Assign the next node of previous node to last node
            del_node.prev.next, self.last.prev = self.last, del_node.prev
            del_node.val = None

        self.cache[key] = DoubleLinkNode(value)
        # Link the node after first node after the assigned node & Change the next node after next node
        second_node = self.first.next
        second_node.prev, self.cache[key].next = self.cache[key], second_node
        self.first.next, self.cache[key].prev = self.cache[key], self.first




class DoubleLinkNode(object):
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


def main():
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))
    cache.put(3, 3)
    print(cache.get(2))
    cache.put(4, 4)
    print(cache.get(1))
    print(cache.get(3))
    print(cache.get(4))



# ["LRUCache","get","put","get","put","put","get","get"]
# [[2],[2],[2,6],[1],[1,5],[1,2],[1],[2]]
def test():
    cache = LRUCache(2)
    cache.put(2, 1)
    cache.put(2, 2)
    print(cache.get(2))
    cache.put(1, 1)
    cache.put(4, 1)
    print(cache.get(2))


if __name__ == '__main__':
    test()
    # main()