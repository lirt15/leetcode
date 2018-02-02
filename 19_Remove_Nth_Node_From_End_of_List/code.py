class Solution(object):
	def removeNthFromEnd(self, head, n):
		if head.next==None:return []
		re_head=tp=head
		for i in range(n-1):
			tp=tp.next
		cnt,cnt_head=0,None
		while tp.next!=None:
			tp=tp.next
			if cnt!=0:
				cnt_head=cnt_head.next
			else:
				cnt_head,cnt=head,1
		if cnt_head==None:
			return head.next
		cnt_head.next=cnt_head.next.next
		return re_head