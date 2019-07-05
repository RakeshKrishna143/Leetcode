class Solution:
    
    def longestPalindrome(self, s: str) -> str:
        if not s: return s
        def ispalindrome(a):
            if a==a[::-1]:
                return True
            else:
                return False


        b={}
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                if s[i]==s[j]:
                    if ispalindrome(s[i:j+1]):
                        b[len(s[i:j+1])]=s[i:j+1]
        return b[max(b)] if b!={} else s[0]
        
