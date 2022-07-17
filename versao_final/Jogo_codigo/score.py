class Score:
    def __init__(self):
        self.__score = 0
        
    @property 
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        self.__score = score

    def update(self):
        self.__score += 1
