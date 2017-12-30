class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """

        stk = []
        ans = 0
        if len(ops)==0: return ans

        for i in ops:
            if i=='D':
                ans+=2*stk[-1]
                stk.append(2*stk[-1])
            elif i=='C':
                ans-=stk.pop(-1)
            elif i=='+':
                ans+=stk[-1]+stk[-2]
                stk.append(stk[-1]+stk[-2])
            else:
                stk.append(int(i))
                ans += int(i)
        return ans
        
