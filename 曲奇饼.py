from Pmf import PMF

'''
曲奇饼问题：假设有两碗曲奇饼，碗1包含30个香草曲奇和10个巧克力曲奇，碗2包含香草和巧克力各20个，假设现在随便从某个碗拿了一个曲奇饼，且该曲奇为香草口味，问从碗1取到的概率？？？
'''

class Cookie(PMF):

    def __init__(self,events):
        PMF.__init__(Cookie)
        for event in events:
            self.set(event,1)
        self.normalize()

    mixes = {
            '碗1':{'香草':0.75,'巧克力':0.25},
            '碗2':{'香草':0.5,'巧克力':0.5}
            }

    def likelihood(self,data,event):
        mix = self.mixes[event]
        like = mix[data]
        return like

    def update(self,data):
        for event in self.kv.keys():
            like = self.likelihood(data,event)
            self.mult(event,like)
        self.normalize()

if __name__ == "__main__":
    events = ['碗1','碗2']
    cookie = Cookie(events)
    cookie.update('香草')
    print(cookie)

    events = ['碗1','碗2']
    cookie = Cookie(events)
    cookie.update('香草')
    cookie.update('巧克力')
    cookie.update('巧克力')
    print(cookie)
