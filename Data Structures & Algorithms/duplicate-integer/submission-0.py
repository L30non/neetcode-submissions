class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_nums_list = set(nums)
        if len(new_nums_list) != len(nums):
            return True
        else:
            return False


nums = [1,2,3,3]

solution = Solution()


print(solution.hasDuplicate(nums))



        
            
        