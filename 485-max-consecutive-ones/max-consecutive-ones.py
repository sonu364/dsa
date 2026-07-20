from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        maximum = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                counter += 1
                maximum = max(maximum, counter)
            else:
                counter = 0

        return maximum
