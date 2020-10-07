
V=7
G=[[1,3,5],[0,2,6],[1,3],[0,2,4],[3,5],[0,4,6],[1,5]]

color=[0 for _ in range(V)]    #頂点の色

def dfs(v,c):
    color[v]=c
    for i in range(len(G[v])):
        #隣接している頂点が同じ色ならfalse
        if(color[G[v][i]]==c):
            return false
        #隣接している頂点がまだ塗られていないなら-cで塗る
        if(color[G[v][i]]==0 and not dfs(G[v][i],-c)):
            return false
    #全ての頂点を塗れたらTrue
    return True

for i in range(V):
    if(color[i]==0):
        #まだ頂点iが塗られていなければ1で塗る
        if(not dfs(i,1)):
            print("No")
            break
else:
    print("Yes")
