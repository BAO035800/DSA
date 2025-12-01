from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        x = 0
        y = n
        while n != 0 and i < len(flowerbed):
            left = 0 if i == 0 else flowerbed[i-1]
            right = 0 if i == len(flowerbed)-1 else flowerbed[i+1]

            if flowerbed[i] == 0 and left == 0 and right == 0:
                n -= 1
                x += 1
                flowerbed[i] = 1
            i += 1
        return x == y

if __name__ == "__main__":
    sol = Solution()
    flowerbed_input = input("Nhập danh sách flowerbed (ví dụ 1,0,0,0,1): ")
    flowerbed = [int(x.strip()) for x in flowerbed_input.split(",")]
    n = int(input("Nhập số lượng hoa cần trồng n: "))
    result = sol.canPlaceFlowers(flowerbed, n)
    print("Output:", result)
