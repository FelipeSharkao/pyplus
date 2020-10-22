from abc import ABC, abstractmethod, abstractproperty

def var(store, f=property):
    def getter(self):
        return self.__dict__[store]
    
    def setter(self, val):
        self.__dict__[store] = val
    
    def deleter(self):
        del self.__dict__[store]
    
    return f(getter, setter, deleter)

class AbstractForeachIter(ABC):
    key = var('_key', abstractproperty)
    val = var('_val', abstractproperty)
    
    @abstractmethod
    def __skip__(self):
        self.val += self.step
    
    @abstractmethod
    def __previous__(self):
        self.val -= self.step


class ForeachInterface:
    @property
    def next(self):
        return None
    
    @property
    def repeat(self):
        return False
    
    @property
    def stop(self):
        return True
    
    @property
    def skip(self):
        self.__skip__()
        return self.next
    
    @property
    def previous(self):
        self.__previous__()
        return self.repeat