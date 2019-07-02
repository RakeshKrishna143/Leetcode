s='abcabcb'
a=[]
b=[]

for i in range(len(s)):
    j=i+1
    a.append(s[i])
    while j<=len(s)-1:
        if s[j] not in a:
            a.append(s[j])
            j+=1
        else:
            b.append(''.join(a))
            a.clear()
            break

print(a)
b.append(''.join(a))
print(b)
        
    
