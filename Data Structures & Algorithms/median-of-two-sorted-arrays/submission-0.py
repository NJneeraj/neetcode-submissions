class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = [nums1, nums2] if len(nums1) < len(nums2) else [nums2, nums1]
        total = len(A) + len(B)
        half = total // 2
        l, r = 0, len(A)

        while True:
            i = (l + r) // 2
            j = half - i

            aLeft = float("-inf") if i == 0 else A[i - 1]
            aRight = float("inf") if i == len(A) else A[i]
            bLeft = float("-inf") if j == 0 else B[j - 1]
            bRight = float("inf") if j == len(B) else B[j]

            if aLeft <= bRight and bLeft <= aRight:
                if total % 2 == 0:
                    return (max(aLeft, bLeft) + min(aRight, bRight)) / 2
                else:
                    return min(aRight, bRight)
            elif aLeft > bRight:
                r = i - 1
            else:
                l = i + 1
