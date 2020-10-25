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
    def __next__(self):
        pass
    
    @abstractmethod
    def __prev__(self):
        pass
    
    @abstractmethod
    def __stop__(self):
        pass
    
    @abstractproperty
    def isended(self):
        pass


class ForeachInterface:
    def next(self):
        self.__next__()
        if self.isended:
            self.__stop__()
        return True
    
    def skipone(self):
        self.next()
        if not self.isended:
            self.next()
    
    def again(self):
        return True
    
    def prev(self):
        self.__prev__()
        return True
    