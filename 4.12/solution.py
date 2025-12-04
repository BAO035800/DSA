from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float('inf')
        for x in nums:
            if x <= first:
                first = x
            elif x <= second:
                second = x
            else:
                return True
        return False

s = input("Nhập mảng số, cách nhau bởi dấu cách: ")
nums = list(map(int, s.split()))
solution = Solution()
result = solution.increasingTriplet(nums)
print("Kết quả:", result)
