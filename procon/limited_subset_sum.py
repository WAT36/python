n=3
a=[3,5,8]
m=[3,2,2]
K=17

dp=[[False for _ in range(K+1)] for _ in range(n+1)]
dp[0][0]=True

for i in range(n):
    for j in range(K+1):
        if(dp[i][j]):
            k=0
            while j+k*a[i]<=K:
                dp[i+1][j+k*a[i]]=True
                k+=1
#    print(dp[i])
#print(dp[n])

print(dp[n][K])