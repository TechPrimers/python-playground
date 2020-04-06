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
#     def twoSum(self, nums, target):
#         a ={}
#         for i, num in enumerate(nums):
#             if target-num in a:
#                 return [a[target - num], i]
#             else:
#                 a[num] = i