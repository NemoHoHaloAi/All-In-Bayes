from Suite import Suite

class Train(Suite):
    def __init__(self,events):
        self.kv={}
        for event in events:
            self.set(event,1./event)
        self.normalize()

    def likelihood(self,data,event):
        if data>event:
            return 0
        return 1./event

if __name__ == "__main__":
    events = range(1,1001) # 假设火车头数量为1~1000等概率的任何值
    train = Train(events)
    train.update(60)
    print('火车头数量概率最大值：',train.max())
    print('火车头数量后验概率分布均值：',train.mean())
    train.plot()

    print('Condition: 60')
    events = range(1,201) # 假设火车头数量为1~1000等概率的任何值
    train = Train(events)
    train.update(60)
    print('火车头数量后验概率分布均值：',train.mean())
    events = range(1,501) # 假设火车头数量为1~1000等概率的任何值
    train = Train(events)
    train.update(60)
    print('火车头数量后验概率分布均值：',train.mean())
    events = range(1,1001) # 假设火车头数量为1~1000等概率的任何值
    train = Train(events)
    train.update(60)
    print('火车头数量后验概率分布均值：',train.mean())
    events = range(1,5001) # 假设火车头数量为1~1000等概率的任何值
    train = Train(events)
    train.update(60)
    print('火车头数量后验概率分布均值：',train.mean())

    print('Condition: 60 30 90')
    events = range(1,201) # 假设火车头数量为1~1000等概率的任何值
    train = Train(events)
    train.update(60);train.update(30);train.update(90)
    print('火车头数量后验概率分布均值：',train.mean())
    events = range(1,501) # 假设火车头数量为1~1000等概率的任何值
    train = Train(events)
    train.update(60);train.update(30);train.update(90)
    print('火车头数量后验概率分布均值：',train.mean())
    events = range(1,1001) # 假设火车头数量为1~1000等概率的任何值
    train = Train(events)
    train.update(60);train.update(30);train.update(90)
    print('火车头数量后验概率分布均值：',train.mean())
    events = range(1,5001) # 假设火车头数量为1~1000等概率的任何值
    train = Train(events)
    train.update(60);train.update(30);train.update(90)
    print('火车头数量后验概率分布均值：',train.mean())
