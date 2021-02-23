s=input()
a=list(map(int,input().strip().split()))
s1=list(map(str,input().strip().split()))
s2=list(map(str,input().strip().split()))
l1=[]
l2=[]
l3=[]
l=list(s)
l4=[]
p=''
for i in range(len(s1)):
    l1.append(len(s1[i]))
for i in range(len(a)):
    k=a[i]+l1[i]
    for j in range(a[i],k):
        p+=s[j]
    l2.append(p)
    p=''
for i in range(len(l2)):
    if(s1[i]==l2[i]):
        k=a[i]+l1[i]
        for j in range(a[i],k):
            if(j>=len(s)):
                break
            else:
                l3.append(l[j])
    else:
        continue

res = [i for i in l if i not in l3]
d=list(res)
for i in range(len(a)):
    if(s1[i]==l2[i]):
        d.insert(a[i],s2[i])
print(''.join(d))
