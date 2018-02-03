# Definition for singly-linked list.
# class ListNode(object):
#	 def __init__(self, x):
#		 self.val = x
#		 self.next = None

class Solution(object):
	def mergeTwoLists(self, l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""
		if l1==None and l2==None:return None
		head2=head1=ListNode(0)
		while l1!=None or l2!=None:
			if l1==None:
				head2.next=l2
				head2=head2.next
				l2=l2.next
			elif l2==None:
				head2.next=l1
				head2=head2.next
				l1=l1.next
			elif l1.val>l2.val:
				head2.next=l2
				head2=head2.next
				l2=l2.next
			else:
				head2.next=l1
				head2=head2.next
				l1=l1.next
		return head1.next