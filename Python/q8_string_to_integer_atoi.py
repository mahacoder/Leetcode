class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """

        l = len(str)
        if l==0:
            return 0

        str = str.strip()
        l = len(str)
        neg = False
        if str[0]=='-':
            neg = True
            str = str[1:]
            l = len(str)
        elif str[0]=='+':
            str = str[1:]
            l = len(str)

        flag = True

        trail = -1
        for i in range(l):
            c = str[i]
            if ord('0')<=ord(c)<=ord('9'):
                pass
            else:
                flag = False
                trail = i
                break

        if not flag:
            str = str[:trail]
            l = len(str)

        ans = 0
        lead = False
        idx = -1
        for i in range(l):
            if str[0]=='0':
                lead = True
            if lead:
                if str[i] != '0':
                    idx = i
                    break
        if lead:
            str=str[idx:]
            l = len(str)

        for i in range(l):
            c = str[i]
            ans += 10**(l-i-1)*(ord(c)-ord('0'))

        if neg: ans= -1*ans

        if -2147483648>ans: return -2147483648
        if 2147483647<ans: return 2147483647


        return ans
        
