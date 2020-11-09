INF=float("inf")

#入力
n=5
d=[[INF for _ in range(n)] for _ in range(n)]

n=5
d=[[INF,3,INF,4,INF],[INF,INF,5,INF,INF],[4,INF,INF,5,INF],[INF,INF,INF,INF,3],[7,6,INF,INF,INF]]

#DP
dp=[[-1 for _ in range(n)] for _ in range(2**n)]
#経路
route="0"

def rec(S,v,r):
    if(dp[S][v] >= 0):
        return dp[S][v],r
    
    if(S == 2**n - 1 and v == 0):
        #全ての頂点を訪れて戻ってきた
        dp[S][v] = 0
        return dp[S][v],r
    
    res = INF
    ans_route=r
    for u in range(n):
        #uがまだ訪れてない? -> Sの2^u桁目が0
        if d[v][u] != INF and (not (S >> u & 1)):
            #次にuに移動する
            res_u,res_route=rec(S | 1 << u , u , r+" -> "+str(u))
            #uに移動した結果の重みが小さいならばその結果を保存する
            if(res>res_u + d[v][u]):
                res=res_u + d[v][u]
                ans_route=res_route
    dp[S][v] = res
    return dp[S][v],ans_route

ans,route=rec(0,0,route)
print("答:{0},経路:{1}".format(ans,route))