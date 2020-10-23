#最小値計算に影響を与えないほどの大きい値
MAX=10**9

class SegmentTree:
    def __init__(self,n):
        self.segtree=[MAX for _ in range(2**n - 1)]

    #k番目の値をaに変更
    def update(self,k,a):
        k+=(2**n)-1
        self.segtree[k]=a
        #登りながら更新
        while k>0:
            k=(k-1)//2
            self.segtree[k]=min(self.segtree[2*k+1],self.segtree[2*k+2])

    #[a,b)の最小値を求める
    #kは節点の番号、l,rはその節点が対応している区間[l,r)のこと。
    #一番最初(根)の時はquery(a,b,0,0,n)とする。
    def query(a,b,k,l,r):
        #[a,b)と[l,r)が交差しなければ、MAXを返す
        if(r<=a or b<=l):
            return MAX
        
        #[a,b)が[l,r)を完全に含んでいれば、節点の値を返す
        if(a<=l and r<=b):
            return self.segtree[k]
        else:
            #そうでない時は、2つの子の最小値を返す
            vl=self.query(a,b,2*k+1,l,(l+r)//2)
            vr=self.query(a,b,2*k+2,(l+r)//2,r)
            return min(vl,vr)


