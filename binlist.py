class BinList():
	def explode(self,number,fixedLength=0):
		self.number=number
		tobin = lambda n: n>0 and [n&1]+tobin(n>>1) or []
		self.binlist=tobin(number)
		self.binlist.reverse()
		if len(self.binlist)<fixedLength:
			for i in range(fixedLength-len(self.binlist)):
				self.binlist.insert(0,0)
		self.isbipolar=False
		return self.binlist
		
	def implode(self,binlist):
		self.binlist=binlist
		self.number = int("".join(str(x) for x in binlist), 2)
		self.isbipolar=False
		return self.number

	def hammingdistance(self,other):
		if len(self.binlist) != len(other.binlist):
			return None
		if self.isbipolar:
			self.uniploar()
		if other.isbipolar:
			other.uniploar()
		return sum(s != o for s, o in zip(self.binlist, other.binlist))
	
	def bipolar(self):
		if not self.isbipolar:
			bp=lambda x: -1 if (x<1) else 1
			self.binlist=[bp(x) for x in self.binlist]
			self.isbipolar=True
		
	def unipolar(self):
		if self.bipolar:
			up=lambda x: 0 if (x<1) else 1
			self.binlist=[up(x) for x in self.binlist]
			self.isbipolar=False

	def norm(self):
		if self.isbipolar:
			self.unipolar()
		return sum(self.binlist)
		
	def complement(self):
		if self.isbipolar:
			self.unipolar()
		comp=lambda x: 0 if (x==1) else 1
		return [comp(x) for x in self.binlist]	
		
	def differ(self,other):
		if len(self.binlist) != len(other.binlist):
			return None
		if self.isbipolar:
			self.uniploar()
		if other.isbipolar:
			other.uniploar()
		dif=lambda x,y: 1 if(x!=y) else 0
		return [dif(s,o) for s, o in zip(self.binlist, other.binlist)]

if __name__ == '__main__':
	"""
	Test code. The expected output is:
	
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1]
		[1, 0, 1, 1, 0, 1]
		49
		49
		3
		[1, 1, 0, 0, 0, 1]
		[0, 1, 0, 1, 0, 1]
		2
		[1, 1, -1, -1, -1, 1]
		[1, 1, 0, 0, 0, 1]
		21
		3
		[0, 1, 0, 1, 0, 1]
		[1, 0, 1, 0, 1, 0]	
		[0, 0, 0, 0, 0, 0]
		[0, 1, 0, 1, 0, 1]
	"""
	
	# Test fixed length list with padding
	bl=BinList()
	bl.explode(45,16)
	print(bl.binlist)
	# Test with smallest possible length 
	bl.explode(45)
	print(bl.binlist)
	# Test imploding a list to a number
	al=BinList()
	al.implode([1,1,0,0,0,1])
	print(al.number)
	# Test with some extra padding
	al.implode([0,0,0,0,0,1,1,0,0,0,1])
	print(al.number)
	# Test Hamming distance between two lists
	x=BinList()
	y=BinList()
	x.implode([1,1,0,0,0,1])
	y.implode([1,0,1,1,0,1])
	print(x.hammingdistance(y))
	# Test Hamming distance between a list and a number
	y.explode(21,6)
	print(x.binlist)
	print(y.binlist)	
	print(x.hammingdistance(y))
	# Test bipolar conversion
	x.bipolar()
	print(x.binlist)
	# Test unipolar conversion
	x.unipolar()
	print(x.binlist)
	x.implode(y.binlist)
	print(x.number)
	# Test norm
	print(x.norm())
	# Test complement
	print(x.binlist)
	print(x.complement())
	# Test difference
	print(x.differ(y))
	y.implode(x.differ(y))
	print(x.differ(y))
