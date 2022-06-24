class Map:
    def __init__(self):
        self.__map1 = [
        '                            ',
        '                            ',   
        '                            ',    
        ' XX    XXX           XX     ',    
        ' XX                         ',    
        ' XXXX         XX         XX ',                    
        ' XXXX       XX              ',
        ' XX    X  XXXX    XX  XX    ',
        '       X  XXXX    XX  XXX   ',
        'P    XXXX  XXXXXX  XX  XXXX ',
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

    def gravity_effect(self, obj):
        obj.direction.y += Map().gravity
        obj.rect.y += obj.direction.y
