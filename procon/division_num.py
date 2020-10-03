n=10
m=10
M=(10**9)+7

dp=[[0 for _ in range(n+1)] for _ in range(m+1)]

dp[0][0]=1
print(dp[0])
for i in range(1,m+1):
    for j in range(n+1):
        if(j-i>=0):
            dp[i][j]=(dp[i-1][j]+dp[i][j-1])%M
        else:
            dp[i][j]=dp[i-1][j]
    print(dp[i])

