#最小値計算に影響を与えないほどの大きい値
MAX=10**9

class SegmentTree(n):
    def __init__(self,n):
        self.segtree=[MAX for _ in range(2**n - 1)]

    #k番目の値をaに変更
    #def update(k,a):

