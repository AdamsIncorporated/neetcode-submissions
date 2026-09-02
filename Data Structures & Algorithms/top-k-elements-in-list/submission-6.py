class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        from collections import defaultdict

        counts = defaultdict(int)

        for i, num in enumerate(nums):
            counts[num] += 1
        

        # Sort by frequency (value of the dict)
        sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)

        # Extract the top k keys
        return [num for num, freq in sorted_counts[:k]]