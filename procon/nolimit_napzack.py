#個数制限なしナップザック問題

#個数,最大の重さ
n,W=map(int,input().split())
#価値と重さ
v=[]
w=[]

#vi,wiでi番目の品物の価値と重さ
for i in range(n):
    vi,wi=map(int,input().split())
    v.append(vi)
    w.append(wi)

#dp
dp=[[0 for _ in range(W+1)] for _ in range(n+1)]

#計算
for i in range(n):
    for j in range(W+1):
        k=0
        while(k*w[i]<=j):
            dp[i+1][j] = max(dp[i+1][j],dp[i][j-k*w[i]]+k*v[i])
            k+=1

#答え
print(dp[n][W])