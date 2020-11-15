class edge:
    def __init__(self,to,cap,rev):
            self.to=to
            self.cap=cap
            self.rev=rev

#入力(頂点の数)
V=0

#グラフ
G=[]
#DFSですでに使われたかのフラグ
used=[False for _ in range(V)]

#fromからtoへ向かう容量capの辺をグラフに追加する
def add_edge(f,t,cap):
    

