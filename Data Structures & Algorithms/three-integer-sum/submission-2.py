class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums)- 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l +=1
                    while nums[l] == nums[l -1 ] and l < r:
                        l += 1
        return res
# if the sum is greater on the sorted list, then we need to move the right pointer down.

# the extended while condition is for checking so duplicates dont exist when checking two pointers. It will ignore previous sorted indices and continue.

    

# context
# need to return a triple array that returns 0, ust be distinct values.



# algorithm
# that checks distinct values
# duplicate triplet values
# return no input if no values sum up to 0 --> hashset of triplet values created, so nested loops



# sorting takes extra
# time: O(nlogn) + O(n^2)
# space: O(1) or O(n) depends on sorting being extra space