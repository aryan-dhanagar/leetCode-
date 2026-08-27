class Solution(object):
    def twoSum(self, nums, target):
        n = len(nums)
        hash_map = {}
        for i in range(n):
            remains = target - nums[i]
            
            if remains in hash_map:
                return [hash_map[remains],i]
            hash_map[nums[i]] = i
