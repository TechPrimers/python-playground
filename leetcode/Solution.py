from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for j in range(0, len(nums)):
            for i in range(0, len(nums)):
                if (i!=j):
                    sumOf=nums[j] + nums[i]
                    if (sumOf == target):
                        return j, i
# Enumeration is faster than this