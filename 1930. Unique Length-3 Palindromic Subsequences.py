class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        letters = set(s)
        res = 0

        for letter in letters:
            i, j = s.index(letter), s.rindex(letter)
            candidates = set()

            for k in range(i + 1, j):
                candidates.add(s[k])

            res += len(candidates)

        return res