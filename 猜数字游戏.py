class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        countA, countB = 0, 0
        lis = []
        charsA = list(secret)
        charsB = list(guess)
        for i in range(len(charsA)):
            lis.append(charsA[i])
            if lis[i] == charsB[i]:
                lis[i] = 'a'
                countA += 1
        for i in range(len(charsB)):
            if lis[i] != 'a' and charsB[i] in lis:
                lis[lis.index(charsB[i])] = 'b'
                countB += 1
        return str(countA) + 'A' + str(countB) + 'B'
