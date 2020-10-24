from .iter import ForeachIterRange


def foreach_range(a, b=None, step=1):
    def inner(method):
        start = 0 if b is None else a
        end = a if b is None else b
        next = abs(step)
        next *= 1 if end > start else -1
        iter = ForeachIterRange(start, step)

        while iter.val < end:
            flag = method(iter)
            if flag is iter.next or flag is None:
                iter.val += next
            elif flag is iter.stop:
                break
            elif flag is not iter.repeat:
                raise ValueError

        del method
        return None

    return inner
