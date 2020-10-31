from .iter import foreachiter


def foreach(*args):
    def wrapper(func):
        iter = foreachiter(*args)

        while not iter.isended:
            if not func(iter):
                iter.next()

        del func
        return None
    return wrapper
