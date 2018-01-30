class Solution(object):
	def addTwoNumbers(self, l1, l2):
		cnt=0
		flag=0
		head=ListNode(0)
		tp=head
		start=True
		while True:
			cnt=(l1.val+l2.val+flag)%10
			flag=(l1.val+l2.val+flag)>=10
			if start:
				head.val=cnt
				start=False
			else:
				tp.next=ListNode(cnt)
				tp=tp.next
			if l1.next==None and l2.next==None and flag==0:
				break

			if l1.next==None:	l1=ListNode(0)
			else:				l1=l1.next

			if l2.next==None:	l2=ListNode(0)
			else:				l2=l2.next

		return head