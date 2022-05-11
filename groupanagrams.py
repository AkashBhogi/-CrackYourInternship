class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={};a=[]
        for i in strs:
            k=i[:]
            i=list(i);i.sort();r="".join(i)
            try:
                d[r].append(k)
            except:
                d[r]=[k]
        for i in d:
            a.append(d[i])
        return a
