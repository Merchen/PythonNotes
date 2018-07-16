
import heapq

heap, data = [], [0, 4, 5, 6, 3, 2, 1, 7, 8, 9]

for n in data:  # heapify(data)列表快速堆化
    heapq.heappush(heap, n)  # 压入堆, heap = [0, 3, 1, 6, 4, 5, 2, 7, 8, 9]

assert heapq.heapreplace(heap, 6) == 0  # 弹出最小元素，并压入新元素

while len(heap):
    heapq.heappop(heap)  # 弹出堆,[1,2,3,4,5,6,6,7,8,9]