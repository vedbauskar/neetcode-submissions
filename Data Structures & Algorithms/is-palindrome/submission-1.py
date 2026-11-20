class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True
        
    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or 
                ord('0') <= ord(c) <= ord('9'))
        



# 





# context
# need to have alphanumeric + numbers
# output must be return true or false

# test cases
# 


# algorithm
# check from both sides of the index
# [ 1   1   1   1   1   1]
#   ^                      
#                       ^

#compare each letter if its the same, if it is continue, if not output false

# given code changes function to work for alphanumeric case, adding or removing spaces when needed or changing to lowercase for all

# heres a proposition for str, extra memory case since theres already a palindrome/duplicate function
#       newStr = """
#           for c in s:
#              if c.isalnum():
#                   newStr += c.lower()
#           return newStr == newStr[::-1] 
#              

# create a dummy string for memoery, check if string has alphanumeric, if it does add it to newstring and make it lower
# compare newstring to reverse string with funciton [::-1], checks from backwards
