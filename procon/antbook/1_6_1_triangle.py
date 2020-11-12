print("n:",end="")
n=int(input())
print("a:",end="")
a=list(map(int,input().split()))

ans=0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            ai,aj,ak=sorted([a[i],a[j],a[k]])
            if(ai+aj>ak and ai+aj+ak>ans):
                ans=ai+aj+ak
print(ans)