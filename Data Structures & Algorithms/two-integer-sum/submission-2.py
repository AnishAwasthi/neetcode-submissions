class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # val:index

        for i,n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
            # you want two indexes to be returned, current and the match diff
                return [prevMap[diff], i]
            prevMap[n] = i


