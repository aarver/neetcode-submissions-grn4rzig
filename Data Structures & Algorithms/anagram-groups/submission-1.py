class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myDict = {}
        for s in strs:
            ss = ''.join(sorted(s))
            if ss not in myDict:
                myDict[ss] = []
            myDict[ss].append(s)
        return list(myDict.values())