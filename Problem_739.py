# 739. Daily Temperatures

class Solution(object):
    def dailyTemperatures(self, T):
        if len(T) == 0 or T is None:
            return []
        rst = [0] * len(T)
        stack = []
        for i in range(len(T)):
            while stack and T[i] > T[stack[-1]] :
                rst[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return rst




def main():
    test_input = [73, 74, 75, 71, 69, 72, 76, 73]
    solution = Solution()
    print(solution.dailyTemperatures(test_input))

if __name__ == '__main__':
    main()