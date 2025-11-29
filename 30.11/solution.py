from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        i = 0
        res = []
        m = max(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= m:
                res.append(True)
            else:
                res.append(False)
            i += 1
        return res
candies = list(map(int, input("Nhập candies:").split()))
extraCandies = int(input("Nhập extraCandies: "))
sol = Solution()
output = sol.kidsWithCandies(candies, extraCandies)
print("Kết quả:", output)
