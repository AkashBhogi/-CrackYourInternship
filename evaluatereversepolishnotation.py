class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        a=[int(tokens[0])]
        for i in range(1,len(tokens)):
            if tokens[i]=="+":
                a.append(a.pop(-2)+a.pop(-1))
            elif tokens[i]=="-":
                a.append(a.pop(-2)-a.pop(-1))
            elif tokens[i]=="*":
                a.append(a.pop(-2)*a.pop(-1))
            elif tokens[i]=="/":
                a.append(int(a.pop(-2)/a.pop(-1)))
            else:
                a.append(int(tokens[i]))
        return a[0]
