class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        x = s.split(" ")
        for i in x[::-1]:
            if i != "":
                return len(i)
                break
        return 0
