import sys

class Memoize:
	def __init__(self, funct):
		self.funct = funct;
		self.cache = {}
	def __call__(self, *args):
		if not self.cache.has_key(args):
			self.cache[args] = self.funct(*args)
		return self.cache[args]
		
def prettyPrinting(substr, str):
	if len(substr) == 0:
		print(str)
		return True
	flag = False
	for i in range(1, len(substr)+1):
		flag = ((substr[:i] in Dictionary) and prettyPrinting(substr[i:], str + " " + substr[:i])) or flag
	return flag

# Start Execution
if (len(sys.argv) == 1):
	print("USAGE: " + sys.argv[0] + " <string to test>\n")
	exit()

goodString = ""
prettyPrinting = Memoize(prettyPrinting)
Dictionary = set( line.strip() for line in open("dictionary.txt"))
print(prettyPrinting(sys.argv[1], ""))