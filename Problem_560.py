class Solution:
    def subarraySum(self, nums, k):
        rst, tmp = 0, 0
        mem = {0 : 1}
        for num in nums:
            tmp += num
            rst += mem[tmp-k] if (tmp-k) in mem else 0
            mem[tmp] = 1 if tmp not in mem else mem[tmp] + 1
        return rst



def main():
    test_input = [1,1,1]
    solution = Solution()
    print(solution.subarraySum(test_input,2))

if __name__ == '__main__':
    main()

# 1 2 3
#