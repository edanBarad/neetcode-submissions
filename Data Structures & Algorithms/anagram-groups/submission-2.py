from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        for word in strs:
            added = False
            for l in result:
                if Counter(word) == Counter(l[0]):
                    
                        l.append(word)
                        added = True
            if not added: result.append([word])
        return result