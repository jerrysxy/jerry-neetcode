from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        result = []

        for index, number in counts.most_common(k):
            result.append(index)
        return result

