215	Kth Largest Element in an Array


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        nums.sort(reverse = True) # 1

        #2
        heap = []
        for num in nums:
            heapq.heappush(heap,num)

            if len(heap)>k:
                heapq.heappop(heap)
                    

        return heap[0]

