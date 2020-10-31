from abc import ABCMeta, abstractmethod, abstractproperty

_pairs = dict()

def var(store, f=property):
    def getter(self):
        return self.__dict__[store]

    def setter(self, val):
        self.__dict__[store] = val

    def deleter(self):
        del self.__dict__[store]

    return f(getter, setter, deleter)


class ForeachIterMeta(ABCMeta):
    @classmethod
    def __prepare__(cls, name, bases, **kargs):
        return super().__prepare__(name, bases, **kargs)

    def __new__(cls, name, bases, kargs):
        return super().__new__(cls, name, bases, kargs)

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

        defaultdict = {
            '_stopped': False,
            'isended': isended,
            'dostop': lambda self: None,
            'stop': stop,
            'next': next,
            'skipone': skipone,
            'prev': prev,
        }

        cls = ForeachIterMeta(cls.__name__, (cls,) + cls.__bases__, {**cls.__dict__, **defaultdict})

        for x in types:
            if type(x) is tuple:
                _pairs[x] = cls
            elif type(x) is list:
                _pairs[tuple(x)] = cls
            else:
                _pairs[tuple([x])] = cls

        return cls
    return wrapper

def foreachiter(*args):
    types = tuple(type(x) for x in args)

    if types in _pairs.keys():
        return _pairs[types](*args)

    raise TypeError
