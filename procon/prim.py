INF=float("inf")

# 設定（ユーザ側で入力）
V=0     #頂点数
cost=[[INF for _ in range(V)] for _ in range(V)]    #cost[i][j]:頂点iから頂点jへのコスト

V=5
cost=[[0,2,5,6,INF],[2,0,1,INF,9],[5,1,0,INF,10],[6,INF,INF,0,4],[INF,9,10,4,0]]

# 設定（入力しない）
ans_cost=[[INF for _ in range(V)] for _ in range(V)]  #cost_x[i][j]:(最小全域木の)頂点iから頂点jへのコスト
min_cost=[INF for _ in range(V)]                    #min_cost[i]:Xから頂点iへの最小コスト
y_nearest_x=[INF for _ in range(V)]                 #y_nearest_x[i]:頂点iへのコストが最も低いXの頂点
used=[False for _ in range(V)]                      #used[i]:頂点iがXに含まれているか示す
for i in range(V):
    ans_cost[i][i]=0

#初めの点の初期設定
min_cost[0]=0
y_nearest_x[0]=0

while True:
    v=-1
    
    #Xに属さない頂点のうちXからの辺のコストが最小になる頂点を探す
    for u in range(V):
        if(not used[u] and (v==-1 or min_cost[u] < min_cost[v])):
            v=u

    #全て見終わったら終了
    if(v==-1):
        break

    #頂点vをXに追加する
    used[v]=True
    ans_cost[v][y_nearest_x[v]]=cost[v][y_nearest_x[v]]
    ans_cost[y_nearest_x[v]][v]=cost[y_nearest_x[v]][v]

    #xからの最終コスト更新
    for u in range(V):
        if(cost[v][u]<min_cost[u]):
            min_cost[u]=cost[v][u]
            y_nearest_x[u]=v

print(ans_cost)


