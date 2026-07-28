class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]):
        seen = set()
        duplicates = set()

        for num in nums:
            if num in seen:
                duplicates.add(num)
            else:
                seen.add(num)

        return list(duplicates)
