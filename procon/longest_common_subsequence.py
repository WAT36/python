s=input() #文字列s
t=input() #文字列t

dp=[[0 for _ in range(len(t)+1)] for _ in range(len(s)+1)]
for i in range(len(s)):
    for j in range(len(t)):
        if(s[i]==t[j]):
            dp[i+1][j+1] = max(dp[i][j]+1,dp[i+1][j],dp[i][j+1])
        else:
            dp[i+1][j+1] = max(dp[i+1][j],dp[i][j+1])

print(dp[len(s)][len(t)]) #sとtの最長共通部分文字列の長さ = 答え