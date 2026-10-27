class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res



# context 
# 2 <= len(nums) <= 100,000
# -30 <=( nums) <= 30
# no division at all
# [1, 2, 4, 6] --> [48, 24, 12, 8]
# must display an product of all elements, none skipped

#test cases:
# must fit between a 32 bit integer
# num indexes cannot be more than 30 or less than -30
# 2 < 100,000 num length
# if input has 1, cannot have duplicate values. skip to next highest permutation

# 
# 
# [1, 2, 4, 6]
#           ^
# will input, 1 x 2 x 4 x 6 = 48
# then will input 4 x 6 = 24
# then will input 2 x 6 = 12
# then will input 2 x 4 = 8

#
