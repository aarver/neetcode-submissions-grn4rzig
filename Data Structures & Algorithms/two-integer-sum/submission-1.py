class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            d[nums[i]] = i 
        
        for i in range(len(nums)):
            dif = target - nums[i]
            if dif in d and d[dif] != i:
                return [i, d[dif]]
        
        # ---brute force---

        # for i in range(len(nums)):            
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]

        