class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = sorted(s)
        sorted_t = sorted(t)
        if sorted(s) == sorted(t):
            return True
        else:
            return False