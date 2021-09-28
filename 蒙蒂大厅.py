from Pmf import PMF
from Suite import Suite

'''
蒙蒂大厅问题：有三扇门，门后均有奖品，但只有一个门后奖品为汽车，其他两个都是小奖品，玩家随机选择一扇门，此时会打开两外两扇中没有汽车的一个门展示给玩家，并询问玩家是否要更换自己的选择，问换或者不换，中奖的概率均为多少？？？
'''

class MontyHall(Suite):
    def likelihood(self,data,event):
        '''
        P(B|A)
        data: 主持人打开的门
        event: 候选的门
        '''
        if event==data:
            return 0 # 对于门2来说，由于门2被打开，因此奖品必然不在它后面，则其似然概率降为0，即P(主持人打开门2|奖品在门2)=0
        elif event=='门1':
            return 0.5 # 对于门1来说，如果奖品在其背后，则门2被打开的概率为0.5，即P(主持人打开门2|奖品在门1)=0.5 
        else:
            return 1 # 对于门3来说，如果奖品在其背后，则门2被打开的概率为1，即P(主持人打开门2|奖品在门3)=1

if __name__ == "__main__":
    # 假设用户首先选择了门1
    events = ['门1','门2','门3']
    montyHall = MontyHall(events)
    print(montyHall)
    montyHall.update('门2')
    print(montyHall)
    montyHall.update('门3')
    print(montyHall)
