
https://leetcode.com/problems/reverse-nodes-in-k-group/

215. Kth Largest Element in an Array

https://leetcode.com/problems/reverse-nodes-in-k-group/

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

 

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5




class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseKGroup(head: ListNode, k: int) -> ListNode:
    if not head or k == 1:
        return head
    
    # 1. 哨兵节点，方便处理头节点变化的情况
    dummy = ListNode(0)
    dummy.next = head
    prev_group_end = dummy
    
    while True:
        # 2. 找到当前组的结尾
        kth_node = get_kth(prev_group_end, k)
        if not kth_node:
            break
        
        next_group_start = kth_node.next
        
        # 3. 反转当前组（需要记录当前组的开头，反转后它会变成结尾）
        curr = prev_group_end.next
        prev = next_group_start # 这一步很巧妙，直接让原组头的 next 指向下一组开头
        
        for _ in range(k):
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
            
        # 4. 把反转后的部分接回原链表
        # 此时 prev 是原 kth_node，即新组的头
        # tmp_start 是原 curr，即反转后的组尾
        tmp_start = prev_group_end.next
        prev_group_end.next = kth_node
        prev_group_end = tmp_start
        
    return dummy.next

def get_kth(curr, k):
    while curr and k > 0:
        curr = curr.next
        k -= 1
    return curr 