class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen_items = []
        for i,n in enumerate(nums):
            if n in seen_items:
                return True
            seen_items.append(n)
        return False