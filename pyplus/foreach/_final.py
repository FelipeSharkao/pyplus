from ._range import foreach_range
from ._list import foreach_list

def foreach(*args):
    _type = type(args[0])
    if _type is int:
        return foreach_range(*args)
    elif _type is list:
        return foreach_list(*args)
    else:
        raise TypeError
