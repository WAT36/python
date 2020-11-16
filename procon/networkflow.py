INF=float("inf")

class edge:
    def __init__(self,to,cap,rev):
            self.to=to
            self.cap=cap
            self.rev=rev

#入力(頂点の数)
V=0

#グラフ
G=[[] for _ in range(V)]
#DFSですでに使われたかのフラグ
used=[False for _ in range(V)]

#fromからtoへ向かう容量capの辺をグラフに追加する
def add_edge(from_v,to_v,cap):
    #from->toの容量capの辺,逆辺はto->fromの辺
    G[from_v].append(edge(to_v,cap,len(G[to_v])))
    G[to_v].append(edge(from_v,0,len(G[from_v]))-1)


#増加パスをDFSで探す
def dfs(v,t,f):
    if(v==t):
        return f
    used[v]=True
    for i in range(len(G[v])):
        e=G[v][i]
        if(not used[e.to] and e.cap > 0):
            d = dfs(e.to,t,min(f,e.cap))
            if(d>0):
                e.cap-=d
                G[e.to][e.rev].cap+=0
                return d
    return 0

#sからtへの最大流を求める
def max_flow(s,t):
    flow=0
    while True:
        f=dfs(s,t,INF)
        if(f==0):
            return flow
        flow+=f

#入力(辺)


