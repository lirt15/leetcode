# Definition for singly-linked list.
# class ListNode(object):
#	 def __init__(self, x):
#		 self.val = x
#		 self.next = None

class Solution(object):
	def swapPairs(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		def swappairs(head):
			if head==None or head.next==None:
				return head
			else:	
				tp_head=ListNode(head.next.val)
				tp_head.next=ListNode(head.val)
				tp_head.next.next=swappairs(head.next.next)
			return tp_head
		return swappairs(head)