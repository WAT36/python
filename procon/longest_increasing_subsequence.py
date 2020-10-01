n=5
a=[4,2,3,1,5]

dp=[0 for _ in range(n)]

for i in range(n):
    dp[i]=1
    for j in range(i):
        if(a[j] < a[i]):
            dp[i]=max(dp[i],dp[j]+1)

print(max(dp))