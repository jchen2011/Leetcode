class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        newList = []

        for x in range(n):
            newList.append(nums[x])
            newList.append(nums[x + n])

        return newList
