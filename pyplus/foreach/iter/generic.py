from abc import ABC, abstractmethod, abstractproperty

_pairs = {}


def var(store, f=property):
    def getter(self):
        return self.__dict__[store]

    def setter(self, val):
        self.__dict__[store] = val

    def deleter(self):
        del self.__dict__[store]

    return f(getter, setter, deleter)


class AbstractForeachIter(ABC):
    @classmethod
    def __prepare__(metacls, name, bases, **kargs):
        dict = super.__prepare__(name, bases, **kargs)

        @property
        def isended(self):
            return self._stopped
        
        def stop(self):
            if not self._stopped:
                self.__stop__()
                self._stopped = True
            return True

        def next(self):
            self.__next__()
            return True

        def skipone(self):
            self.__next__()
            return False

        def again(self):
            return True

        def prev(self):
            self.__prev__()
            return True

        return dict + {
            '_stopped': False,
            'isended': isended,
            '__stop__': lambda self: None,
            'stop': stop,
            'next': next,
            'skipone': skipone,
            'again': again,
            'prev': prev,
        }

    def __new__(metacls, name, bases, namespace, **kargs):
        return super().__new__(metacls, name, bases, namespace)

    def __init__(cls, name, bases, namespace, types, **kargs):
        super().__init__(name, bases, namespace)
        for x in types:
            _pairs[tuple(x)] = cls

    key = var('_key', abstractproperty)
    val = var('_val', abstractproperty)

    @abstractmethod
    def __next__(self):
        pass

    @abstractmethod
    def __prev__(self):
        pass


def foreachiter(*args):
    types = (type(x) for x in args)

    if types in _pairs:
        return _pairs[types](*args)

    raise TypeError
