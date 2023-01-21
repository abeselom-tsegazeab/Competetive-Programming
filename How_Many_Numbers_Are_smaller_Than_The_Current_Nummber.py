
class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        smlnum = []
        for i in nums:
            num =0
            for j in nums:
                if j < i:
                    num +=1
            smlnum.append(num)
        return smlnum
            
