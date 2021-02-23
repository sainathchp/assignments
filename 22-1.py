s=input()
l1=[]
l2=[]
c=0
for i in range(len(s)):
    if(s[i].isdigit()==True):
        l1.append(s[i])
for i in range(0,10):
    for j in range(len(l1)):
        if(int(i)==int(l1[j])):
            c+=1
    l2.append(c)
    c=0
print(*l2)
