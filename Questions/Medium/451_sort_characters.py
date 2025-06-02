import heapq
from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)

        heap = [(-count, char) for char, count in freq.items()]
        heapq.heapify(heap)

        result = []
        while heap:
            count, char = heapq.heappop(heap)
            result.append(char * -count)

        return ''.join(result)
