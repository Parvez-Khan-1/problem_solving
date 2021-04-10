# https://leetcode.com/problems/valid-parentheses/


class Solution:

    def isValid(self, s: str):
        stack = []
        order_map = {'(': ')', '{': '}', '[': ']'}

        for ch in s:
            if ch in ('(', '[', '{'):
                stack.append(ch)
            else:
                if not stack:
                    return False

                prev_element = stack.pop()
                if order_map.get(prev_element) != ch:
                    return False
        return not stack


exp = "(]"
s = Solution()
print(s.isValid(exp))
