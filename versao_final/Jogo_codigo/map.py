class Map:
    def __init__(self):
        self.__map1 = {
            'ground': '../mapas/Level1/level1_Ground.csv',
            'coins' : '../mapas/Level1/level1_Coins.csv',
            'enemys' : '../mapas/Level1/level1_Enemys.csv',
            'limiter' : '../mapas/Level1/level1_Limiter.csv',
            'player' : '../mapas/Level1/level1_Player.csv'
                }

    @property
    def map1(self):
        return self.__map1



