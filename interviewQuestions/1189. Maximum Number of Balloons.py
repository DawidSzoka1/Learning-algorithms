from collections import Counter
from operator import itemgetter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        t = Counter(text)
        words = itemgetter('b', 'a', 'l', 'o', 'n')(t)
        if words[0] == 0 or words[1] == 0 or words[2] < 2 or words[3] < 2 or words[4] == 0:
            return 0
        else:
            return min(words[0], words[1], words[2] // 2, words[3] // 2, words[4])
