


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        def helper(gird, row, col):
            if row < 0 or row >= len(gird) or col < 0 or col >= len(gird[0]) or gird[row][col] == "0" :
                return
            gird[row][col] = "0"
            helper(gird, row + 1, col)
            helper(gird, row, col + 1)
            helper(gird, row - 1, col)
            helper(gird, row, col - 1)

        if len(grid) == 0 or grid == None:
            return 0

        rst = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    rst += 1
                    # change the surround 1 to 0
                    helper(grid, row, col)

        return rst


def main():
    test = [["1","1","1"],["0","1","0"],["1","1","1"]]
    solution = Solution()
    print(solution.numIslands(test))

if __name__ == '__main__':
    main()