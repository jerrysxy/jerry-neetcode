from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        result = []
        for number, freq in counts.most_common(k):
            result.append(number)
        return result