import os,sys

'''
PMF：概率质量函数类，用于描述一组数据的分布，即值与概率的对应关系；

例子，质地均匀的六面骰子的PMF如下：
1 -> 1/6
2 -> 1/6
3 -> 1/6
4 -> 1/6
5 -> 1/6
6 -> 1/6
'''

class PMF(object):
    def __init__(self):
        self.kv = {}

    def set(self,event,prob):
        self.kv[event] = prob

    def incr(self,event,times):
        self.kv[event] = self.kv.get(event,0)+times

    def mult(self,event,prob):
        self.kv[event] = self.kv[event]*prob

    def normalize(self):
        total_prob = sum([v for k,v in self.kv.items()])
        self.kv = {k:v/total_prob for k,v in self.kv.items()}

    def prob(self,event):
        return self.kv[event]

    def __str__(self):
        return str(self.kv)

if __name__ == "__main__":
    pmf = PMF()
    for i in range(1,7,1):
        pmf.set(i,1/6.)
    print(pmf.kv)

    pmf = PMF()
    for i in range(1,7,1):
        pmf.incr(i,1)
    pmf.normalize()
    print(pmf.kv)

    pmf = PMF()
    pmf.set('B1',1/2.)
    pmf.set('B2',1/2.)
    pmf.mult('B1',0.75)
    pmf.mult('B2',0.5)
    pmf.normalize()
    print(pmf.prob('B1'))
