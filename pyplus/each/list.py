from .generic import eachiter


@eachiter((list, tuple), '?', int)
class EachIterList:
    def __init__(self, list, step=1):
        self._list = list
        self.step = step

    _key = 0

    @property
    def key(self):
        return self._key
    
    @key.setter
    def key(self, x):
        if x >= len(self.list) or x < 0:
            self._ended = True
            self._key = None
        else:
            self._key = x
    
    @property
    def val(self):
        if self._ended:
            return None
        return self.list[self.key]
    
    @val.setter
    def val(self, x):
        if self._ended:
            return None
        self.list[self.key] = x
    
    _ended = False
    
    @property
    def isended(self):
        return self._ended
    
    @isended.setter
    def isended(self, x):
        self._ended = bool(x)
    
    @property
    def step(self):
        return self._step

    @step.setter
    def step(self, x):
        self._step = abs(x)
    
    @property
    def list(self):
        return self._list