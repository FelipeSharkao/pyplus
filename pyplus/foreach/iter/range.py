from ._generic import AbstractForeachIter, var


class ForeachIterRange(mataclass=AbstractForeachIter, types=[
    (int)
    (int, int),
    (int, int, int),
]):
    @property
    def step(self):
        return self._step

    @step.setter
    def step(self, val):
        if val:
            self._step = val
        else:
            raise ValueError

    key = var('_key')
    key = var('_val')

    def __init__(self, start, step=1):
        self.val = start
        self.key = 0
        self.step = step

    def __skip__(self):
        self.val += self.step
        self.key += 1

    def __previous__(self):
        self.val -= self.step
        self.key -= 1
