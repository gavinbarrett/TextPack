class Compressor:
	
	def __init__(self, string):
		self.table = {}
		self.encoded = []
		self.words = string.split(' ')

	def compress(self):
		#
		return self.encode_words() + self.encode_table()

	def encode_words(self):
		#
		idx = 0
		for word in self.words:
			if word in self.table:
				self.encoded.append(self.table[word])
				continue
			else:
				self.table.setdefault(word, idx)
				self.encoded.append(idx)
				idx += 1
		return bytes(self.encoded)
	
	def encode_table(self):
		#
		return b'|' + '|'.join(self.table.keys()).encode()
