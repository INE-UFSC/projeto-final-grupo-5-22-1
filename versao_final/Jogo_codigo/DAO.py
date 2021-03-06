from abc import ABC
import pickle
import sys

class DAO(ABC):
    def __init__(self, datasource = ''):
        self.__datasource = datasource
        self.__cache = {}
        try:
            self.load()
        except FileNotFoundError:
            self.dump()
    
    def  dump(self):
        arch = open(self.__datasource, 'wb')
        pickle.dump(self.__cache, arch)
        arch.close()
    
    def load(self):
        arch = open(self.__datasource, 'rb')
        self.__cache = pickle.load(arch)
        arch.close()

    def add(self, key, obj):
        self.__cache[key] = obj
        print("adiconado score")
        self.dump()
        
    def remove(self, key):
        try:
            self.__cache.pop(key)
            self.dump()
            return True
        except KeyError:
            raise          

    def get(self, key):
        try:
            return self.__cache[key]
        except KeyError:
            print('Chave não encontrada', arch = sys.stderr)
            raise KeyError

    def get_all(self):
        return self.__cache.items()