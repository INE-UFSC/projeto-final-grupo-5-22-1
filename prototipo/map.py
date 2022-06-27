class Map:
    def __init__(self):
        self.__map1 = [
        '                            ',
        '                            ',   
        'L  L  L   L         L  L    ',    
        ' XX    XXX           XX     ',    
        ' XXCC        L EL       L  L',    
        ' XXXX       C XX    C    XX ',                    
        ' XXXXL  LL  XX   L  LL EL   ',
        '      XX  XXXX    XX  XX    ',
        '      XX  XXXXCC  XX  XXX   ',
        'P   EXXXX  XXXXXX  XX  XXXX ',
        'XXXXXXXX  XXXXXX  XX  XXXX  ',                                      
                                        ]
        self.__ground_size = 64
        self.__gravity = 0.5

    @property
    def map1(self):
        return self.__map1

    @property
    def ground_size(self):
        return self.__ground_size

    @property
    def gravity(self):
        return self.__gravity

