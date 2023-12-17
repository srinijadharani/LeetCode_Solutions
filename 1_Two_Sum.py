class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_numbers = set()
        for i, num in enumerate(nums):
            comp = target - num

            if comp in seen_numbers:
                return [nums.index(comp), i]
            seen_numbers.add(num)

        return []
