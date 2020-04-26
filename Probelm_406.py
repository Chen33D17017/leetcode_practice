class Solution:
    def reconstructQueue(self, people):
        if len(people) == 0 or people == None:
            return []
        rst = []
        people.sort(key=lambda x: (-x[0], x[1]))
        for person in people:
            rst.insert(person[1], person)
        print(rst)

def main():
    test = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
    solution = Solution()
    solution.reconstructQueue(test)

if __name__ == '__main__':
    main()