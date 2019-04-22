DELIM = '>'

inputFile = input("Enter the input file name: ")
outputFile = input("Enter the output file name: ")

fIn = open(inputFile, "r")
fOut = open(outputFile, "w")

lineNo = 0
for inLine in fIn:
    lineNo += 1
    fOut.write("%4s%-2s%s" % (str(lineNo), DELIM, inLine))

fIn.close
fOut.close
