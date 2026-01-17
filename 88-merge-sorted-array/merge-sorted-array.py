class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        #base case to return early if n or m ==0
        if n==0:
            return
        elif m==0:
                nums1[:n] = nums2[:n]
                return
        #using a 3 pointer approach
        pointer_one = m - 1 #pointer for nums1
        pointer_two = n-1 #pointer for nums2
        write_position = m+n-1 #pointer for where to write values

        #break when the nums2 runs out
        while pointer_two >= 0:
            #ensure that nums1 still has values to be compared to
            #check if nums1 > nums2
            if pointer_one >= 0 and nums1[pointer_one] > nums2[pointer_two]:
                nums1[write_position] = nums1[pointer_one]
                pointer_one -=1
            else:
                #now nums2 > nums1 so write to the free position at the end
                nums1[write_position] = nums2[pointer_two]
                pointer_two-=1
            write_position -= 1   