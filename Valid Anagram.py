'''
Engineer's Revolution

Program to check whether two strings 
are anagram to each other 

'''

s = 'TRIANGLE'
t = 'IntegraL'

def isAnagram(s,t):
    return sorted(s.lower())==sorted(t.lower())

print(isAnagram(s, t))
