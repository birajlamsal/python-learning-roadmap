import heapq


def heap_sort(arr):
    heap = []
    for item in arr:
        heapq.heappush(heap, item)

    sorted_arr = []
    while heap:
        sorted_arr.append(heapq.heappop(heap))

    return sorted_arr
