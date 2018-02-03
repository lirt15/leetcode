class Solution(object):
	def mergeKLists(self, lists):
		if len(lists)==0:return []
		tp_head=head=ListNode(0)
		node_val,None_cnt=[],0
		for i in range(len(lists)):
			if lists[i]==None:
				node_val.append(10**5)
				None_cnt+=1
			else:
				node_val.append(lists[i].val)

		while None_cnt!=len(lists):
			min_value=min(node_val)
			min_index=node_val.index(min_value)

			tp_head.next=lists[min_index]
			tp_head=tp_head.next

			lists[min_index]=lists[min_index].next	
			if 	lists[min_index]==None:
				None_cnt+=1
				node_val[min_index]=10**5
			else:
				node_val[min_index]=lists[min_index].val
		return head.next