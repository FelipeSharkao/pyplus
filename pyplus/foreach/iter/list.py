from ._generic import AbstractForeachIter


class ForeachIterList(mataclass=AbstractForeachIter, types=[
    (list),
    (list, int),
]):
    @property
    def list(self):
        return self._list

    @property
    def key(self):
        return self._key
    
    @key.setter
    def key(self, x):
        if x >= len(self.list) or x < 0:
            raise IndexError
        else:
            self._key = x
    
    @property
    def val(self):
        if self.isended:
            return None
        return self.list[self.key]
    
    @val.setter
    def val(self, x):
        if self.isended:
            return None
        self.list[self.key] = x
    
    @property
    def step(self):
        return self._step

    @step.setter
    def step(self, x):
        self._step = abs(x)

    def __init__(self, list, step=1):
        self._list = list
        self._key = 0
        self.step = step
    
    def __next__(self):
        try:
            self.key += self.step
        except IndexError:
            self.key = len(self.list) - 1
            self.stop()
    
    def __prev__(self):
        try:
            self.key -= self.step
        except IndexError:
            self.key = 0
