class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        string = list(s)
        def reverse(s, e):
            i, j = s, e
            while i<j:
                string[i], string[j] = string[j], string[i]
                i+=1
                j-=1

        slow, fast = 0, 0
        while fast<len(string):
            if string[fast] != ' ':
                fast+=1
            else:
                reverse(slow, fast-1)
                slow=fast+1
                fast+=1

        reverse(slow, fast-1)
        return ''.join(string)
