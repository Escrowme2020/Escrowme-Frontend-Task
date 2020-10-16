from django.test import TestCase

# Create your tests here.

class Odd(object):
	"""docstring for Odd"""
	def __init__(self, arg):
		self.arg = arg
	def __me(cls):
		print('Ran secured function', cls.arg)
	def call_me(self):
		self.__me()

dd = Odd(23)
dd.call_me()
