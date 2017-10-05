import sys

with open(sys.argv[1],'r') as textInput:
	
	for line in textInput:
		if "*** START OF THIS PROJECT GUTENBERG EBOOK" in line:
			with open(sys.argv[2],'w') as textOutput:
				for line in textInput:
					while("End of the Project Gutenberg EBook" not in line):
						textOutput.write(line)
					break