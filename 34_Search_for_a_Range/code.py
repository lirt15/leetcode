class Solution(object):
	def searchRange(self, nums, target):
		lo,hi=0,len(nums)-1
		mid=int((lo+hi)/2)
		if not nums:return[-1,-1]
		while nums[lo]!=target and nums[hi]!=target and nums[mid]!=target:
			if hi-lo<2:
				return[-1,-1]
			if nums[mid]<target:
				lo=mid+1
			elif nums[mid]>target:
				hi=mid-1
			mid=int((lo+hi)/2)
		if nums[lo]==target:mid=lo
		if nums[hi]==target:mid=hi
		i,j=mid-1,mid
		while i>=0 and nums[i]==target:
			i-=1
		while j<=len(nums)-1 and nums[j]==target:
			j+=1
		return [i+1,j-1]
