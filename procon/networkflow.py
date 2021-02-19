INF=float("inf")

class edge:
    def __init__(self,to,cap,rev):
            self.to=to
            self.cap=cap
            self.rev=rev

#頂点の数
V=0

#グラフ
G=[]
#DFSですでに使われたかのフラグ
used=[]

#初期化
def init(v):
    global G
    global used
    G=[[] for _ in range(v)]
    used=[False for _ in range(v)]

#fromからtoへ向かう容量capの辺をグラフに追加する
def add_edge(from_v,to_v,cap):
    global G
    #from->toの容量capの辺,逆辺はto->fromの辺
    G[from_v].append(edge(to_v,cap,len(G[to_v])))
    G[to_v].append(edge(from_v,0,len(G[from_v])-1))


#増加パスをDFSで探す
def dfs(v,t,f):
    global G
    global used
    if(v==t):
        return f
    used[v]=True
    for i in range(len(G[v])):
        e=G[v][i]
        if(not used[e.to] and e.cap > 0):
            d = dfs(e.to,t,min(f,e.cap))
            if(d>0):
                e.cap-=d
                G[e.to][e.rev].cap+=d
                return d
    return 0

#sからtへの最大流を求める
def max_flow(s,t):
    global used
    flow=0
    while True:
        used=[False for _ in range(V)]
        f=dfs(s,t,INF)
        if(f==0):
            return flow
        flow+=f

#初期化
V=5
init(V)

#入力(辺)
add_edge(0,1,10)
add_edge(0,2,2)
add_edge(1,2,6)
add_edge(1,3,6)
add_edge(3,2,3)
add_edge(2,4,5)
add_edge(3,4,8)

#実行
ans=max_flow(0,4)
print(ans)
