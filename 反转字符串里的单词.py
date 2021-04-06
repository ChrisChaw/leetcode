class Solution:
    def reverseWords(self, s: str) -> str:
        if s == '' or len(s) == 0:
            return ''
        li_s = s.strip().split(" ")[::-1]
        res = []
        for i in range(len(li_s)):
            if li_s[i] == '' or li_s[i] == ' ':
                continue
            res.append(li_s[i])
        return " ".join(res)
