class Solution:

    #context:
    # create a string manipulation model that serves to extract strings based on indices
    # must somehow mark boundaries between encoded segmetns 
    # how can we choose the proper seperator?

    # testcases
    # if the string lists to become empty
    
    # alogirthm:
    # one good model for a seperator can be the comma (,), hold a dummy variable in place for encoding again
    # do a count for every character in the encoded string
    # have a hashmap created for every instance of string?
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
        

    def decode(self, s: str) -> List[str]:
        res, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res