class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) #mapping charCount to group anagrams

        for s in strs:
            count = [0] * 26 # every letter gets a count
        
            for c in s:
                count[ord(c) - ord("a")] += 1 
            #use ASCII to check each independent letter and add 
            #the count to be added to key
            res[tuple(count)].append(s) #must be tuple for keys
        return list (res.values()) 
        
