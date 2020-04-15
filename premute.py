
class Solution:
    def permute(self, nums):
        self.ans = []
        def helper(nums, store):
            if len(nums) == 0:
                self.ans.append(store)
                return
            else:
                for i, num in enumerate(nums):
                    tmp = nums[:]
                    tmp.pop(i)
                    helper(tmp, store + [num])

        helper(nums, [])
        return self.ans


def test():
    test_input = [1, 2, 3]
    solution = Solution()
    print(solution.permute(test_input))

if __name__ == '__main__':
    test()
