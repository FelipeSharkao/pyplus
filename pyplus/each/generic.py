from abc import ABCMeta, abstractmethod

_pairs = {}


class EachIterMeta(ABCMeta):
    @classmethod
    def __prepare__(cls, name, bases, **kargs):
        return super().__prepare__(name, bases, **kargs)

    def __new__(cls, name, bases, kargs):
        return super().__new__(cls, name, bases, kargs)

    @property
    @abstractmethod
    def key(self):
        raise NotImplementedError
    
    @property
    @abstractmethod
    def val(self):
        raise NotImplementedError
    
    @property
    @abstractmethod
    def isended(self):
        raise NotImplementedError


def each(*args):
    types = tuple(type(x) for x in args)
    _iter = None

    if types in _pairs:
        _iter = _pairs[types](*args)
    else:
        raise TypeError(f"Cannot find an 'each' implementation with signature {types}.")

    while not _iter.isended:
        yield _iter
        _iter.key += 1


def eachiter(*args):
    def wrapper(cls):
        newcls = EachIterMeta(cls.__name__, (cls,) + cls.__bases__, dict(cls.__dict__))
        del cls

        lst = []
        opt = False
        for x in args:            
            if isinstance(x, str):
                if x == '?':
                    if not opt:
                        opt = True
                    else:
                        raise ValueError("Literal '?' can only be used once.")
                else:
                    raise ValueError(f"Unexpected string '{x}'")
            else:
                if opt:
                    _pairs[tuple(lst)] = newcls
                lst.append(x)
        
        _pairs[tuple(lst)] = newcls

        return newcls
    return wrapper
