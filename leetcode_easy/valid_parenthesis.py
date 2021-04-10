# https://leetcode.com/problems/valid-parentheses/
# Valid Assumption: There wont be any chars/nums except (, {, [, ], }, )


class Solution:
    def isValid(self, s: str):
        stop = True
        original_length = len(s)
        while stop:
            s = s.replace("{}", "")
            s = s.replace("[]", "")
            s = s.replace("()", "")
            if len(s) < original_length:
                original_length = len(s)
            else:
                stop = False
        if len(s) > 0:
            return False
        else:
            return True

exp = "{{}[][[[]]]}"

s = Solution()
print(s.isValid(exp))
