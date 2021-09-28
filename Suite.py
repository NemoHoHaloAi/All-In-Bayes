from Pmf import PMF
import matplotlib.pyplot as plt

class Suite(PMF):
    def __init__(self,events):
        PMF.__init__(Suite)
        for event in events:
            self.set(event,1)
        self.normalize()

    def update(self,data):
        for event in self.kv.keys():
            like = self.likelihood(data,event)
            self.mult(event,like)
        self.normalize()

    def max(self):
        return max(self.kv, key=self.kv.get)

    def min(self):
        return min(self.kv, key=self.kv.get)

    def mean(self):
        '''
        输出后验概率的平均值
        '''
        return sum([k*v for k,v in self.kv.items()])

    def plot(self):
        plt.plot(self.kv.keys(),self.kv.values())
        plt.show()
