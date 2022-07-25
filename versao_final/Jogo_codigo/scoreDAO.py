from DAO import DAO
from score import Score

class ScoreDAO(DAO):
    def __init__(self):
        super().__init__('score.pkl')

    def add(self, score: Score):
        if (score is not None) and (isinstance(score, Score)):
            super().add(score.id, score)
   
    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key)

    def find_key(self, id: str):
        for key, score in super().get_all():
            if score.id == id:
                return key
        raise KeyError