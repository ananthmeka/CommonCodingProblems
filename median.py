class Solution:
    def getmedian(self, nums: List[int]) -> float:
        if length1 == 0:
            if even_length:
                median1 = nums[mid_num] + nums[mid_num+1] /2
            else:
                median1 = nums[mid_num] 
        return median1
    
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        length1 = len(nums1)
        length2 = len(nums2)
        full_length = length1 + length2
        mid_num = int(full_length / 2)
        even_length = False
        if full_length % 2:
            even_length = True
        if length1 == 0:
            return self.getmedian(nums2)
        if length1 == 0:
            return self.getmedian(nums1)    
        
        median = 0
        current_length = 0
        sp1 = 0 
        ep1 = length1
        sp2 = 0
        ep2 = length2
        from_one = True
        while current_length < mid_num:
            mid1 = ep1 + sp1 / 2 
            mid2 = ep2 + sp2 / 2
            if num1[mid1] < num2[mid2]:                
                current_length = current_length + mid1 - sp1
                sp1 = mid1
                from_one = True
            else:
                current_length = current_length + mid2 - sp2
                sp2 = mid2
                from_one = False
        if from_one:
            pos1 = num1[mid1]
            pos2 = 0
            if even_length :
                pos2 = num1[mid1+1]
                if num1[mid1+1] < num2[mid2]:
                    pos2 = num2[mid2]
            median = pos1 + pos2/2
        else:
            pos1 = num2[mid2]
            pos2 = 0
            if even_length :
                pos2 = num2[mid2+1]
                if num2[mid2+1] < num1[mid1]:
                    pos2 = num1[mid1]
            median = pos1 + pos2/2
        return median

print(Solution().findMedianSortedArrays([2,6,8,10],[1,3,5]))
