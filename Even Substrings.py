n=int(input())
s=str(input())
c=0
j=0
for i in s:
    if(int(i)%2==0):
        c+=1
        c+=j
    j+=1
print(c)