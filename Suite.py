from Pmf import PMF

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
