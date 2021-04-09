class Solution:
    def validPalindrome(self, s: str) -> bool:
        def checkPalindrome(low, high):
            # 检查原字符串是否是回文字符串
            i, j = low, high
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        # 检查删掉一个字符后 是否是回文字符串
        low, high = 0, len(s) - 1
        while low < high:
            if s[low] == s[high]:
                low += 1
                high -= 1
            else:
                return checkPalindrome(low + 1, high) or checkPalindrome(low, high - 1)
        return True
