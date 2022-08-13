"""Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct."""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        lst_nums = list(set(nums))
        if len(nums) == len(lst_nums):
            return False
        return True