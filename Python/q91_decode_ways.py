class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==0: return 0
        ans = [0]*(len(s)+1)
        flag = False
        ans[0]=1
        for i in range(len(s)):
            if i==0:
                if s[i]=='0': ans[i+1]==0
                else: ans[i+1]=1
            else:
                if s[i]=='0':
                    sub = s[i-1:i+1]
                    if int(sub)>26 or int(sub)<1:
                        flag = True
                        break
                    ans[i+1]=ans[i-1]
                    ans[i]=ans[i-1]
                else:
                    if s[i-1]=='0':
                        ans[i+1]=ans[i]
                    else:
                        sub = s[i-1:i+1]
                        if int(sub)<=26:
                            ans[i+1]=ans[i]+ans[i-1]
                        else:
                            ans[i+1]=ans[i]
        if flag: return 0
        return ans[-1]
