class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        for i in range(n):
            nums1.pop()
        for i in range(n):
            nums1.append(nums2[i])
            nums1.sort()
        print(nums1)
s=Solution()
nums1 =[1,2,3,0,0,0]
m =3
nums2 =[2,5,6]
n =3
s.merge(nums1,m,nums2,n)