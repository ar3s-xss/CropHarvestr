class Crops:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def cropHarvesting(self):
        with open('crops.txt', 'a') as season:
            season.write(f'{self.x}:{self.y}\n')
            season.close()


