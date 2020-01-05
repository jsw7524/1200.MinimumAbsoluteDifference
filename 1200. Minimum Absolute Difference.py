class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr.sort()
        tmp=[]
        for i in range(1 ,len(arr)):
            tmp.append([[arr[i-1], arr[i]], arr[i]-arr[i-1]])
        tmp.sort(key=lambda t: t[1])
        result=[]
        for t in tmp:
            if t[1] == tmp[0][1]:
                result.append(t[0])
        return result

sln=Solution()
assert [[-14,-10],[19,23],[23,27]]==sln.minimumAbsDifference([3,8,-10,23,19,-4,-14,27])
