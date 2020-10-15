INF=float("inf")

#辺
class edge:
    def __init__(self,start,end,cost):
        self.start=start
        self.end=end
        self.cost=cost


#以下、V,E,s,edgesを入力する
V=5     #頂点の数
E=7     #辺の数
s=0     #始点
d  = [-1 for _ in range(V)] # 最短距離

edges = [edge(-1,-1,-1) for _ in range(E)] #辺
edges[0]=edge(0,1,2)
edges[1]=edge(0,2,5)
edges[2]=edge(0,3,6)
edges[3]=edge(1,2,1)
edges[4]=edge(1,4,9)
edges[5]=edge(2,4,10)
edges[6]=edge(3,4,4)

def shortest_path(s):
    for i in range(V):
        d[i] = INF
    d[s]=0
    while True:
        update=False
        for i in range(E):
            e=edges[i]
            if(d[e.start] != INF and d[e.end] > d[e.start] + e.cost):
                d[e.end] = d[e.start] + e.cost
                update = True
        if(not update):
            break

shortest_path(s)
print(d)