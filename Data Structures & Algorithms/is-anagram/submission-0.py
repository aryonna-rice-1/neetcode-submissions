from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_counts = Counter(s)
        t_counts = Counter(t)
        for letter, s_freq in s_counts.items():
            if s_freq != t_counts[letter]:
                return False
        return True