from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        f = Counter(s)
        a = Counter(t)
        return a == f
