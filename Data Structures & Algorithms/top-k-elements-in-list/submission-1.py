from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        result = []
        counts = Counter(nums)
        for num, _ in counts.most_common(k):
            result.append(num)
        return result
        