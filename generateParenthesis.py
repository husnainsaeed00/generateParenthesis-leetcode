class Solution:
    def generateParenthesis(self, n):
        result = []
        self.generate(n, n, "", result)
        return result

    def generate(self, open_count, close_count, current, result):
        if open_count == 0 and close_count == 0:
            result.append(current)
            return

        if open_count > 0:
            self.generate(open_count - 1, close_count, current + "(", result)

        if close_count > open_count:
            self.generate(open_count, close_count - 1, current + ")", result)
solution = Solution()

print(solution.generateParenthesis(3))
# Output: ["((()))","(()())","(())()","()(())","()()()"]

print(solution.generateParenthesis(1))
# Output: ["()"]
