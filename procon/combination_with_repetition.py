n=3
m=3
a=[1,2,3]
M=(10**9)+7

dp=[[0 for _ in range(m+1)] for _ in range(n+1)]

for i in range(n+1):
    # 1個も選ばない方法は1通り
    dp[i][0]=1

for i in range(1,n+1):
    for j in range(1,m+1):
        if(j-1-a[i-1]>=0):
            dp[i][j]=(dp[i][j-1]+dp[i-1][j]-dp[i-1][j-1-a[i-1]])%M
        else:
            dp[i][j]=(dp[i][j-1]+dp[i-1][j])%M

print(dp[n][m])