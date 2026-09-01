class Solution:
    def isPalindrome(self, s: str) -> bool:
        basket = []
        for i in s.lower():
            if i.isalnum():
                basket.append(i)
        basket_wno_space = "".join(basket)
    
        return basket_wno_space == basket_wno_space[::-1]