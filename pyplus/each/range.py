from .generic import eachiter


@eachiter(int, '?', int, int)
class EachIterRange:
    def __init__(self, a, b=None, step=1):
        if b:
            self._start = a
            self._end = b
        else:
            self._start = 0
            self._end = a
        self.val = self.start
        self.step = step
    
    @property
    def key(self):
        return (self._val - self.start) // self.step
    
    @key.setter
    def key(self, x):
        self.val = x * self.step + self.start
    
    @property
    def val(self):
        if self._ended:
            return None
        return self._val
    
    @val.setter
    def val(self, x):
        if self._ended:
            return None
        if x >= self.end or x < self.start:
            self._ended = True
            self._val = None
        else:
            self._val = x
    
    _ended = False
    
    @property
    def isended(self):
        return self._ended
    
    @isended.setter
    def isended(self, x):
        self._ended = bool(x)
    
    @property
    def start(self):
        return self._start

    @property
    def end(self):
        return self._end
    
    @property
    def step(self):
        return self._step

    @step.setter
    def step(self, x):
        if (self.end - self.start) % 1 is not x % 1:
            raise ValueError
        else:
            self._step = x
