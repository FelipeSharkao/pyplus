from .iter import foreach_iter as iter


def foreach(*args):
    def wrapper(func):
        _iter = iter(*args)

        while not _iter.isended:
            if not func(_iter):
                _iter.next()

        del func
        return None
    return wrapper
