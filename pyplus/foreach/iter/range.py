from .generic import registeriter


@registeriter(
    (int),
    (int, int),
    (int, int, int),
)
class ForeachIterRange:
    @property
    def start(self):
        return self._start

    @property
    def end(self):
        return self._end

    @property
    def key(self):
        return (self._val - self.start) // self.step
    
    @key.setter
    def key(self, x):
        self.val = x * self.step + self.start
    
    @property
    def val(self):
        if self.isended:
            return None
        return self._val
    
    @val.setter
    def val(self, x):
        if self.isended:
            return None
        if x >= self.end or x < self.start:
            raise IndexError
        else:
            self._val = x
    
    @property
    def step(self):
        return self._step

    @step.setter
    def step(self, x):
        if (self.end - self.start) % 1 is not x % 1:
            raise ValueError
        else:
            self._step = x

    def __init__(self, a, b=None, step=1):
        if b:
            self._start = a
            self._end = b
        else:
            self._start = 0
            self._end = a
        self.val = self.start
        self.step = step
    
    def donext(self):
        try:
            self.val += self.step
        except IndexError:
            self.val = self.end - self.step
            self.stop()
    
    def doprev(self):
        try:
            self.val -= self.step
        except IndexError:
            self.val = self._start
