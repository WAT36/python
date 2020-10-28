class BinaryIndexedTree:
    def __init__(self,a):
        #BITを表すリストaを入力
        #ただしaの長さは2**nとする
        #数合わせのためにa[1]~a[len(a)]をBITとする
        self.bit=[0]
        self.bit.extend(a)

    def sum(self,i):
        ans=0
        while i>0:
            ans+=self.bit[i]
            i -= i & -i
        return ans
    
    def add(self,i,x):
        while i<len(self.bit):
            self.bit[i]+=x
            i += i & -i


a=[5,7,3,17,4,5,9,41]
bit_a=BinaryIndexedTree(a)

#i=7までのaの和
print("a[7]までの和:{}".format(bit_a.sum(7)))

print("加える前のBIT:{}".format(bit_a.bit[1:]))

#a[5]に1を足す
bit_a.add(5,1)

print("加えた後のBIT:{}".format(bit_a.bit[1:]))