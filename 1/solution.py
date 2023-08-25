# first solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):
            for j in range(len(nums) - i - 1):
                if (nums[i] + nums[j + i + 1] == target):
                    newArray = []
                    newArray.append(i)
                    newArray.append(j + i + 1)
                    return newArray
