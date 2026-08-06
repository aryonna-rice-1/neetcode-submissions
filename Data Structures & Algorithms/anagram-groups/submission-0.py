from collections import Counter, defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            encoding = [0] * 26
            counts = Counter(word)
            for letter, count in counts.items():
                encoding[ord(letter) - ord('a')] = count
            anagrams[tuple(encoding)].append(word)
        return list(anagrams.values())