#This algorithm use linear search and has a complexity of O(N)

def returnlongestlist(nums1, nums2):
    
    if len(nums1) > len(nums2):
        return nums1
    
    else:
        return nums2
        
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        sorted_list = []
        total_size = len(nums1) + len(nums2)
        i=0; j=0
        
        while i < len(nums1) and j < len(nums2):
            
            if nums1[i] < nums2[j]:
                sorted_list.append(nums1[i])
                i += 1
            
            else:
                sorted_list.append(nums2[j])
                j += 1
                    
        if i == len(nums1) or j == len(nums2): 
            list_to_be_continued = returnlongestlist(nums1[i:], nums2[j:])
            sorted_list = sorted_list.extend(list_to_be_continued)
            
                
        if len(sorted_list)%2 == 0:
            median = float(sorted_list[total_size/2 - 1] +  sorted_list[total_size/2])/2
            
        else:
            
            median = sorted_list[int(total_size/2)]
        
        return median
                