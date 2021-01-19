import heapq

N = int(input())

heap = []

for i in range(N):
    com = int(input())
    if com == 0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap,com)
