class Solution(object):
    def twoSum(self, nums, target):
        l = []
        for i in range(0, len(nums)):
            m = target - nums[i]
            for j in range(0, len(nums)):
                if(i==j):
                    continue
                if(m == nums[j]):
                    l.append(i)
                    l.append(j)
                    return l
        return l
        