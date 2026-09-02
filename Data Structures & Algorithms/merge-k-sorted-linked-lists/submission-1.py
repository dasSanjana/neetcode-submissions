# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(min_heap,(node.val,i,node))
        dummy = ListNode(-1)
        cur = dummy
        while min_heap:
            val , i , smallest_node = heapq.heappop(min_heap)
            cur.next = smallest_node
            cur = cur.next
            if smallest_node.next:
                heapq.heappush(min_heap,(smallest_node.next.val,i,smallest_node.next))
        return dummy.next

            





