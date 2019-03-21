n=int(input())
l=[int(x) for x in input().split()]
c=0
mx=0
for i in range(n):
    if(l[i]==1):
        c+=1
        if(c>mx):
            mx=c
    else:
        c=0
j=0
c1=0
while(l[j]==1):
    c1+=1
    j+=1
j=n-1
c2=0
while(l[j]==1):
    c2+=1
    j-=1
d=c1+c2
print(max(d,mx))