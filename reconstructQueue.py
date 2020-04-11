

class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        rst = []

        people.sort(key=lambda x: (-x[0], x[1]))
        first_i = people[0][0]
        for i, item in enumerate(people):
            if i == 0:
                rst.append(item)
                continue
            h, order = item[0], item[1]
            if len(rst) < item[1]:
                rst.append(item)
            else:
                rst.insert(order,item)
        print(rst)



def test():
    test_input = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
    solution = Solution()
    solution.reconstructQueue(test_input)


if __name__ == '__main__':
    test()