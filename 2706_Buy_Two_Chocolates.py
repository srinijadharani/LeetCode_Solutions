class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        nums = sorted(prices)
        sum_ = nums[0]+nums[1]
        final = money - sum_

        if final >= 0:
            return final
        else:
            return money
