class Solution(object):
	def searchInsert(self, nums, target):
		if not nums:return 0
		lo,hi,mid=0,len(nums)-1,int((len(nums)-1)/2)
		while nums[lo]!=target and nums[hi]!=target and nums[mid]!=target:
			if hi-lo<2:
				if target>nums[hi]:return hi+1
				elif target<nums[lo]:return lo
				else:return lo+1
			if nums[mid]<target:
				lo=mid+1
			elif nums[mid]>target:
				hi=mid-1
			mid=int((lo+hi)/2)
		if nums[lo]==target: return  lo
		if nums[mid]==target: return mid 
		if nums[hi]==target: return  hi

tp=Solution()
print(tp.searchInsert([1,3],2))