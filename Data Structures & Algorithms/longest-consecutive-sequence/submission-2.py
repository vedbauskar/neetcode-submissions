class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            # check if its the start of a sequence
            if (n - 1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest






# context
# must need algorithm in O(n) time
# needs to be a concurrent exactly 1 sequence
# output the amount of sequences


# test cases
# same number
# negative


# algorithm
# create hashmap and add the next value into checking loop
# one loop for going through the array, then checking i
# output will check how many times the hashmap checker is passed