class Decompressor:
	
	def __init__(self, string):
		self.table = {}
		self.encoded = []
		self.compressed = string
	
	def decompress(self, ):
		#
		idx = self.compressed.find(b'|')
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
		new_str = [entries[c] for c in compr]
		print(' '.join(new_str))
