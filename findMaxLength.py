

class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tmp = {0: -1}
        count = 0
        max_length = 0
        test = []
        for i, num in enumerate(nums):
            count += 1 if num else - 1
            test.append(count)
            if count in tmp:
                max_length = max(max_length, i - tmp[count])
            else:
                tmp[count] = i
        return max_length

# -1 [0  1  1  0  1  1  1  0]
# 0 -1  0  1  0  1  2  3  2

def test():
    test_pattern = [0,1,1,0,1,1,1,0]
    solution = Solution()
    print(solution.findMaxLength(test_pattern))

if __name__ == '__main__':
    test()