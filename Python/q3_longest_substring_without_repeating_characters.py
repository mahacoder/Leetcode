from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        l = len(s)
        if l==0: return 0
        map = defaultdict()
        ans = 0
        start = end = 0
        while start<l and end<l:
            c = s[end]
            if c not in map:
                map[c] = 1
                end+=1
            else:
                ans = max(ans, len(map))
                # print(start, end, )
                del map[s[start]]
                start+=1
        ans = max(ans, len(map))
        return ans

        
