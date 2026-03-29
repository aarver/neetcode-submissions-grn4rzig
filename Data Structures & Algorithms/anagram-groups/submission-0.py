class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myDict = defaultdict(list)
        for s in strs:
            sorted_str = ''.join(sorted(s))
            myDict[sorted_str].append(s)
        return list(myDict.values())