class Solution(object):
	def reverseKGroup(self, head, k):
		result=new_head=ListNode(0)
		flag=True
		while flag==True:
			tp_val,tp_head=[],head
			for _ in range(k):
				if head!=None:
					tp_val.append(head.val)
					head=head.next
				else:
					new_head.next=tp_head
					flag=False
			if flag:
				for i in tp_val[::-1]:
					new_head.next=ListNode(i)
					new_head=new_head.next
		return result.next