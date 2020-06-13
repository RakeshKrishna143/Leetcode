''' Given a string s and an integer k.

Return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are (a, e, i, o, u).

 

Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters. '''

#Sliding window method

s = 'eiuaooo'
k = 4

vowel = set('aeiou')
count,m = 0,0

for i,c in enumerate(s):
    count += (c in vowel)
    if i>=k :
        count -= (s[i-k] in vowel)
    m = max(m,count)
print(m)
