import sys
		
def prettyPrinting(string):
	n = len(string)
	
	bResults = set()
	bResults.add(n)
	sResults = {}
	sResults[n] = ""
	
	for i in range(n)[::-1]:
		for j in range(i,n)[::-1]:
			if ((j+1 in bResults) and (string[i:j+1] in Dictionary)):
				bResults.add(i)
				sResults[i] = string[i:j+1] + " " + sResults[j+1]
				break
	
	if (0 in bResults):
		print(sResults[0])
	return (0 in bResults)

# Start Execution
if (len(sys.argv) == 1):
	print("USAGE: " + sys.argv[0] + " <string to test>\n")
	exit()

Dictionary = set( line.strip() for line in open("dictionary.txt"))
print(prettyPrinting(sys.argv[1]))