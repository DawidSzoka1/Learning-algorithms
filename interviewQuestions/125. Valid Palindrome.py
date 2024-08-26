class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        s = s.lower()
        r = len(s) - 1
        while l < r:
            if not s[l].isalpha() and not s[l].isnumeric():
                l += 1
            elif not s[r].isalpha() and not s[r].isnumeric():
                r -= 1
            elif s[l] != s[r]:
                return False
            else:
                l += 1
                r -= 1
        return True