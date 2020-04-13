

class Solution(object):
    def dailyTemperatures(self, T):
        n = len(T)
        rst = [0 for _ in range(n)]
        stack = []
        for i in range(n):
            while stack and T[i] > T[stack[-1]]:
                rst[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return rst

    def dailyTemperatures2(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        rst = [0] * len(T)
        stack = []
        for i in range(len(T)):
            i = len(T) -1 - i
            while len(stack) > 0:
                day, temper = stack[-1][0], stack[-1][1]
                if T[i] >= temper:
                    stack.pop(-1)
                else:
                    break
            if len(stack) == 0:
                rst[i] = 0
            else:
                rst[i] =  day - i
            stack.append((i, T[i]))
        return rst

    def bruteForce(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        rst = []
        for i, item in enumerate(T):
            find = False
            for j in range(i, len(T)):
                print(T[i], T[j])
                if T[i] < T[j]:
                    rst.append(j-i)
                    find = True
                    break
            if not find:
                rst.append(0)
        return rst

def test():
    T = [73, 74, 75, 71, 69, 72, 76, 73]
    # T = [55, 38, 53, 81, 61, 93, 97, 32, 43, 78]
    solution = Solution()
    print(solution.dailyTemperatures(T))

if __name__ == '__main__':
    test()
