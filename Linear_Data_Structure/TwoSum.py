#1. 브루트포스 (가장 복잡 => n제곱)
class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


#2. in을 이용한 탐색 (n제곱이긴한데 1번보다 훨씬 빠름)
    def twoSum2(self, nums, target):
        for i, n in enumerate(nums):
            complement = target - n

            if complement in nums[i+1:]:
                return nums.index(n), nums[i+1:].index(complement) + (i+1)

solution = Solution()
print(solution.twoSum([2,7,11,15],9))
print(solution.twoSum2([2,7,11,15],9))
