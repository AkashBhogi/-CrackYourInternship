class Solution:
    def reverseWords(self, s: str) -> str:
        a=[];b=""
        for i in s:
            if i!=" ":
                b+=i
            else:
                if b!="":
                    a.append(b)
                    a.append(" ")
                    b=""
        if b!="":
            a.append(b)
        for i in range(-1,-len(a)-1,-1):
            if a[i]!=" ":
                if i==-1:
                    break
                else:
                    a=a[:i+1]
                    break
        a.reverse()
        return "".join(a)
