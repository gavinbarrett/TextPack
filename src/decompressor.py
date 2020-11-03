class Decompressor:
	
	def __init__(self, string):
		self.table = {}
		self.encoded = []
		self.compressed = string
	
	def decompress(self):
		# find the boundary of the compressed string
		idx = self.compressed.find(b'|')
		# raise an error if the table can't be located
		if idx == -1:
			raise Exception('Unable to locate compression table.')
		# extract compressed string
		compr = list(self.compressed[:idx])
		# extract compression table
		table = self.compressed[idx:]
		# decode the table and parse entries
		entries = table.decode().split('|')
		# delete empty string at head
		del entries[0]
		# translate the indices to words
		new_str = [entries[c] for c in compr]
		# return the words joined into a string
		return ' '.join(new_str)
