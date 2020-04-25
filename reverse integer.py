'''

Engineer's Revolution
Program to reverse integer 

'''

x = -720

def reverse(x):
    if x>=0:
        r = int(str(x)[::-1])
        
    else:
        r = -int(str(-x)[::-1])
        
    return r if abs(r)<2**31-1 else 0

print(reverse(x))
