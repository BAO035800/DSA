class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u','A','E','I','O','U'}
        list_s = list(s)  
        left, right = 0, len(list_s) - 1
        while left < right:
            if list_s[left] not in vowels:
                left += 1
                continue
            if list_s[right] not in vowels:
                right -= 1
                continue
            list_s[left], list_s[right] = list_s[right], list_s[left]
            left += 1
            right -= 1

        return "".join(list_s)
    
s = input("Nhập chuỗi: ")
solution = Solution()
result = solution.reverseVowels(s)
print("Kết quả đảo nguyên âm:", result)
