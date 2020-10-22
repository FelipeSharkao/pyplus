from iter import ForeachIterList


def foreach_list(l, step=1):
    def inner(method):
        iter = ForeachIterList(l)

        while iter.key < len(iter.list):
            try:
                flag = method(iter)
                if flag is iter.next or flag is None:
                    iter.key += 1
                elif flag is iter.stop:
                    break
                elif flag is not iter.repeat:
                    raise ValueError
            except IndexError:
                break

        del method
        return None

    return inner
