from ._generic import AbstractForeachIter, ForeachInterface, var


@AbstractForeachIter.register
class ForeachIterList(ForeachInterface):
	key = var('_key')

	@property
	def val(self):
		return self.list[self.key]

	@val.setter
	def val(self, val):
		self.list[self.key] = val

	def __init__(self, list):
		self.list = list
		self.step = 1
		self.key = 0

	def __skip__(self):
		self.key += 1

	def __previous__(self):
		self.key -= 1
