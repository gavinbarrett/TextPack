import unittest
from sys import path
path.append('../')
from src.compressor import Compressor
from src.decompressor import Decompressor

class LosslessTester(unittest.TestCase):

	def test_loss_1(self):
		str1 = 'hello there my name is hello there you know my name hello it is it is hello'
		c = Compressor(str1)
		compressed = c.compress()
		d = Decompressor(compressed)
		self.assertEqual(str1, d.decompress())

if __name__ == "__main__":
	unittest.main()
