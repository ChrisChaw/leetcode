class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = 1
            else:
                dic[nums[i]] += 1
        tmp = sorted(dic.items(), key=lambda item: item[1], reverse=True)[:k]
        res = []
        for elem in tmp:
            res.append(elem[0])
        return res
