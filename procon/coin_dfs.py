#coin_dfs.py

#k円、標準入力から
print("k:",end="")
k=int(input())

coin=[1,5,10,50,100,500]

#硬貨の場合分けを深さ優先探索で調べる、iが場合分けした硬貨の枚数、nが現在の金額
def dfs(i,n):

    #全て調べ終わったら判定
    if(i==6):
        return n==k
    
    #coin[i]を使わない場合
    if( dfs(i+1,n) ):
        return True
    
    #coin[i]を使う場合
    if( dfs(i+1,n+coin[i])):
        return True

    #どの場合もTrueにならなかった → 払えないのでFalse
    return False

print(dfs(0,0))