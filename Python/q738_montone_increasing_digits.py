class Solution:
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        n = list(str(N))
        flag = False
        slow, fast = 0, 0
        while slow<len(n) and fast<len(n):
            # print(slow, fast)
            if flag:
                n[slow]='9'
                slow+=1
                continue
            if n[slow]==n[fast]:
                fast+=1
                continue
            elif n[slow]>n[fast]:
                n[slow]=str(int(n[slow])-1)
                flag = True
                slow+=1
            else:
                slow+=1

        return int(''.join(n))
