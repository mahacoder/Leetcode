# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """

        ans = []
        l = len(intervals)
        if l==0: return ans

        intervals = sorted(intervals, key=lambda x: x.start)
        i, j = 0,1

        while j<l:
            i_s, i_e = intervals[i].start, intervals[i].end
            start, end = i_s, i_e
            while j<l and end>=intervals[j].start:
                if intervals[j].end>end: end=intervals[j].end
                j+=1
            ans.append([start, end])
            i=j
            j+=1
        while i<l:
            ans.append(intervals[i])
            i+=1
        return ans

#         intervals = sorted(intervals, key=lambda x: x.start)

#         for i in range(l):
#             i_s, i_e = intervals[i].start, intervals[i].end
#             if i_s is None and i_e is None:
#                 continue
#             for j in range(i+1, l):
#                 j_s, j_e = intervals[j].start, intervals[j].end
#                 if i_s<=j_s<=i_e and j_e>=i_e:
#                     intervals[j].start=intervals[j].end=None
#                     i_e=j_e
#                 elif i_s<=j_s<=i_e and j_e<=i_e:
#                     intervals[j].start=intervals[j].end=None
#                 elif j_s>i_e: break
#             ans.append([i_s, i_e])
#         return ans
                    
