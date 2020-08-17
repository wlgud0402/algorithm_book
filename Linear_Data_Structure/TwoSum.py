#1. 브루트포스 (가장 복잡 => n제곱)
class Solution:
    def twoSum1(self, nums, target_num):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target_num:
                    return [i, j]


solution = Solution()
print(solution.twoSum1([2,7,11,15],9))


