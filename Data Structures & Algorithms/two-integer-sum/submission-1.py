class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            difference = target - num

            if difference in seen:
                return [seen[difference],i]
            
            seen[num] = i

        


nums = [4,5,3]

target = 8

solution = Solution()

print(solution.twoSum(nums,target))

