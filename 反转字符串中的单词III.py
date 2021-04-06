class Solution:
    def reverseWords(self, s: str) -> str:
        li_s = s.split(" ")
        res = []
        for item in li_s:
            reverse_s = item[::-1]
            res.append(reverse_s)
        return " ".join(res)
