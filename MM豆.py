from Suite import Suite

class MMBean(Suite):

    mix94 = {'褐色':0.3,'黄色':0.2,'红色':0.2,'绿色':0.1,'橙色':0.1,'黄褐色':0.1}
    mix96 = {'蓝色':0.24,'黄色':0.14,'红色':0.13,'绿色':0.2,'橙色':0.16,'褐色':0.13}

    def likelihood(self,data,event):
        event = {x.split('-')[0]:x.split('-')[1] for x in event.split(',')}
        bean1,bean2 = data
        like1 = self.mix94[bean1] if event[bean1]=='94' else self.mix96[bean1]
        like2 = self.mix94[bean2] if event[bean2]=='94' else self.mix96[bean2]
        return like1*like2

if __name__ == "__main__":
    events = [{'黄色':'94','绿色':'96'},{'黄色':'96','绿色':'94'}]
    events = ['黄色-94,绿色-96','黄色-96,绿色-94']
    mmBean = MMBean(events)
    print(mmBean)
    mmBean.update(['黄色','绿色'])
    print(mmBean)
