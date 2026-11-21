class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i, num in enumerate(nums):
            for j, num in enumerate(nums):
                if (i == j):
                    continue
                else:
                    checkSum = nums[i] + nums[j]
                    if checkSum == target:
                        return [i,j]

        


nums = [4,5,3]

target = 8

solution = Solution()

print(solution.twoSum(nums,target))

