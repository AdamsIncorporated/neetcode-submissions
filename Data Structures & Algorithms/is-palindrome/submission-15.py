class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ''.join(ch for ch in s if ch.isalnum())
        forward = cleaned.replace(' ', '').lower()
        rev = [s for s in forward][::-1]
        joined_rev = "".join(rev)
        
        if joined_rev != forward:

            return False

        return True