class Solution:
    def firstUniqChar(self, s: str) -> int:
        import collections
        frequency = collections.Counter(s)
        for i, ch in enumerate(s):
            if frequency[ch] == 1:
                return i
        return -1
