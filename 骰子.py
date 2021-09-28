from Suite import Suite

class Dice(Suite):
    def likelihood(self,data,event):
        if data>event:
            return 0
        return 1/event

if __name__ == "__main__":
    dice = Dice([4,6,8,12,20])
    print(dice)
    dice.update(6)
    print(dice)
    dice.update(6)
    dice.update(8)
    dice.update(7)
    dice.update(7)
    dice.update(5)
    dice.update(4)
    print(dice)
