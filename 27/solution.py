class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = len(nums)

        while i < j - 1:
            if nums[i] == nums[i + 1]:
                nums.pop(i)
                j -= 1
                continue

            i += 1

        return len(nums)