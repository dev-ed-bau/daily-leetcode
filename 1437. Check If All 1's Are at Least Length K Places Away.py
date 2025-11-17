class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last_seen_index = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            if last_seen_index != -1:
                if i - last_seen_index - 1 < k:
                    return False
            last_seen_index = i

        return True