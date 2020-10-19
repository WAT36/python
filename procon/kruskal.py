from union_find import UnionFind_fast

INF=float("inf")

#辺
class edge:
    def __init__(self,start,end,cost):
        self.start=start
        self.end=end
        self.cost=cost

def e_comp(e1,e2):
    return e1.cost < e2.cost


# 設定（ユーザ側で入力）
V=0     #頂点数
cost=[[INF for _ in range(V)] for _ in range(V)]    #cost[i][j]:頂点iから頂点jへのコスト

V=5
cost=[[0,2,5,6,INF],[2,0,1,INF,9],[5,1,0,INF,10],[6,INF,INF,0,4],[INF,9,10,4,0]]

# 設定（入力しない）
es=[edge(i,j,cost[i][j]) for i in range(V) for j in range(i+1,V) if cost[i][j] != INF ]
es=sorted(es,key=lambda ei:ei.cost)
ans_cost=[[INF for _ in range(V)] for _ in range(V)]  #cost_x[i][j]:(最小全域木の)頂点iから頂点jへのコスト
uf=UnionFind_fast(V)

for i in range(len(es)):
    ei=es[i]
    if(not uf.same(ei.start,ei.end)):
        uf.unite(ei.start,ei.end)
        ans_cost[ei.start][ei.end]=cost[ei.start][ei.end]
        ans_cost[ei.end][ei.start]=cost[ei.end][ei.start]

print(ans_cost)
