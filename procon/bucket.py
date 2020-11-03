import math
INF=float("inf")

class Bucket:
    def __init__(self,a):
        #元のリスト
        self.a=a
        #平方分割用バケット用意
        b=int(math.sqrt(len(a))//1)
        #１バケットあたりのデータの個数
        self.b=b
        bucket=[]
        b_start=0
        b_end=b
        while True:
            if(b_end>=len(a)):
                bucket.append(min(a[b_start:]))
                break
            else:
                bucket.append(min(a[b_start:b_end]))
                b_start+=b
                b_end+=b
        #バケット
        self.bucket=bucket
    
    #a[s]~a[t]の最小値を求める
    def query(self,s,t):
        ans=INF
        x=s

        #(a[s]~)個々の要素の計算
        if(x%self.b != 0 and x<=t):
            ans=min(ans,self.a[x])
            x+=1
        
        #(a[s]~a[t]が１バケット内のとき)最小値を返す
        if(x>t):
            return ans
        #(そうでないとき)バケット計算
        else:
            while (x+self.b<=t):
                ans=min(ans,self.bucket[x//self.b])
                x+=self.b
        
        #(~a[t])個々の要素の計算
        if(t-x+1==self.b):
            #(a[t]がバケット内の最後の要素であったとき)
            ans=min(ans,self.bucket[x//self.b])
            return ans
        else:
            #そうでないときは１個ずつ見る
            while x<=t:
                ans=min(ans,self.a[x])
                x+=1
            return ans

    #a[i]をxに変更
    def update(self,i,x):
        self.a[i]=x
        #a[i]があるバケットのインデックス
        j=i//self.b
        self.bucket[j]=min(self.bucket[j],x)

a=[5,2,3,7,4,1,9,10]
buc=Bucket(a)

#a[1]~a[4]までの最小値
print("a{0}~a{1}までの最小値:{2}".format(1,4,buc.query(1,4)))

#a[0]を0に変える
buc.update(0,0)
print("バケット:{}".format(buc.a))

