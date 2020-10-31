from abc import ABC, abstractmethod, abstractproperty

_pairs = dict()

def var(store, f=property):
    def getter(self):
        return self.__dict__[store]

    def setter(self, val):
        self.__dict__[store] = val

    def deleter(self):
        del self.__dict__[store]

    return f(getter, setter, deleter)


class ForeachIterMeta(ABC):
    @classmethod
    def __prepare__(metacls, name, bases, **kargs):
        dict = ABC.__prepare__(name, bases, **kargs)

        @property
        def isended(self):
            return self._stopped
        
        def stop(self):
            if not self._stopped:
                self.dostop()
                self._stopped = True
            return self

        def next(self):
            if not self._stopped:
                self.donext()
            return self

        def skipone(self):
            if not self._stopped:
                self.donext()
                self.donext()
            return self

        def prev(self):
            if not self._stopped:
                self.doprev()
            return self

        return dict + {
            '_stopped': False,
            'isended': isended,
            'dostop': lambda self: None,
            'stop': stop,
            'next': next,
            'skipone': skipone,
            'prev': prev,
        }

    def __new__(metacls, name, bases, kargs):
        return ABC.__new__(metacls)

    key = var('_key', abstractproperty)
    val = var('_val', abstractproperty)

    @abstractmethod
    def donext(self):
        pass

    @abstractmethod
    def doprev(self):
        pass

def registeriter(*types):
    def wrapper(cls):
        cls = ForeachIterMeta(cls.__name__, cls.__bases__, cls.__dict__)

        for x in types:
            if isinstance(x, tuple):
                _pairs[x] = cls
            elif isinstance(x, list):
                _pairs[tuple(x)] = cls
            else:
                _pairs[(x)] = cls

        return cls
    return wrapper

def foreachiter(*args):
    types = (type(x) for x in args)

    if types in _pairs:
        return _pairs[types](*args)

    raise TypeError
