from typing import List

class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        """
        Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

        You may assume that each input would have exactly one solution, and you may not use the same element twice.
        
        You can return the answer in any order.
        """
        res = list()
        for i in range(len(nums)):
            right = target - nums[i]
            if right in nums[i+1:]:
                res.append(i)
                res.append(nums.index(right))
                return res
            
