def marsExploration(s):
    c=0
    for i in range(0, len(s), 3):
        print(i)
        if   s[i+0]!="S":
            c+=1
        elif s[i+1]!="O": 
            c+=1
        elif s[i+2]!="S": 
            c+=1
    return c
s = input()
print(marsExploration(s))