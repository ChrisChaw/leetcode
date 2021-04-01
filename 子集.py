class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for num in nums:
            new_sets = []
            for subset in result:
                new_sets.append(subset + [num])
            result.extend(new_sets)
        return result
