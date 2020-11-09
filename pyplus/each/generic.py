from abc import ABCMeta, abstractmethod
from copy import copy 

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

        def readsignature(args, past=[], opt=False):
            last = copy(past)
            args = list(copy(args))

            for i in range(len(args)):
                if isinstance(args[i], tuple) or isinstance(args[i], list):
                    if len(args[i]) > 1:
                        for j in range(1, len(args[i])):
                            nargs = copy(args[i:])
                            nargs[0] = args[i][j]
                            readsignature(nargs, last, opt)
                        args[i] = args[i][0]
                    else:
                        raise ValueError(f"Type union '{args[i]}' should have two types or more.")
                
                if isinstance(args[i], str):
                    if args[i] == '?':
                        if not opt:
                            opt = True
                        else:
                            raise ValueError("Literal '?' can only be used once.")
                    else:
                        raise ValueError(f"Unexpected string '{args[i]}'")
                else:
                    if opt:
                        nargs = copy(args[i + 1:])
                        readsignature(nargs, last, opt)
                    last.append(args[i])
            _pairs[tuple(last)] = newcls

        readsignature(args)

        return newcls
    return wrapper
