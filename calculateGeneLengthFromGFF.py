import sys
#calculate gene length for rpkm/fpkm calculation from gff annotation files
def calculateGeneLengthFromGff(inputfilename, outputfilename):
    inputfile = open(inputfilename, 'r')
    outputfile = open(outputfilename, 'w')
    lengthList = []
    geneId = ""
    for line in inputfile:
        currentGeneIdPosition = line.find("gene_id")
        if currentGeneIdPosition < 0:
            continue
        else:
            lineElements = line.strip().split()
            if lineElements[2] == "exon":
                currentGeneId = getStringTillCharacter(line[currentGeneIdPosition+8:], ";")
                if geneId == currentGeneId:
                    lengthList = lengthList + [[int(lineElements[3]), int(lineElements[4])]]
                else:
                    if geneId != "":
                        lengthListSorted = sorted(lengthList)
                        outputfile.write(geneId + '\t' + str(totalLengthOfIntegerPairs(lengthListSorted)) + '\n')
                        geneId = currentGeneId
                        lengthList = [[int(lineElements[3]), int(lineElements[4])]]
                    else:
                        geneId = currentGeneId
                        lengthList = lengthList + [[int(lineElements[3]), int(lineElements[4])]]
    lengthListSorted = sorted(lengthList)
    outputfile.write(geneId + '\t' + str(totalLengthOfIntegerPairs(lengthListSorted)))

#calculate gene length for rpkm/fpkm calculation from gtf annotation files
def calculateGeneLengthFromGtf(inputfilename, outputfilename):
    inputfile = open(inputfilename, 'r')
    outputfile = open(outputfilename, 'w')
    lengthList = []
    geneId = ""
    for line in inputfile:
        currentGeneIdPosition = line.find("gene_id")
        if currentGeneIdPosition < 0:
            continue
        else:
            lineElements = line.strip().split()
            if lineElements[2] == "exon":
                currentGeneId = getStringTillCharacter(line[currentGeneIdPosition+9:], "\"")
                if geneId == currentGeneId:
                    lengthList = lengthList + [[int(lineElements[3]), int(lineElements[4])]]
                else:
                    if geneId != "":
                        lengthListSorted = sorted(lengthList)
                        outputfile.write(geneId + '\t' + str(totalLengthOfIntegerPairs(lengthListSorted)) + '\n')
                        geneId = currentGeneId
                        lengthList = [[int(lineElements[3]), int(lineElements[4])]]
                    else:
                        geneId = currentGeneId
                        lengthList = lengthList + [[int(lineElements[3]), int(lineElements[4])]]
    lengthListSorted = sorted(lengthList)
    outputfile.write(geneId + '\t' + str(totalLengthOfIntegerPairs(lengthListSorted)))


#input a list of sorted integer pairs eg: [[1, 4], [4, 5], [5, 6], [5, 7]]
#output the non-overlapped length of these pairs. eg: (3-1)+(5-4)+(7-5) = 5
def totalLengthOfIntegerPairs(inputList):
    length = inputList[0][1] - inputList[0][0] + 1
    holdPosition = inputList[0][1]
    for i in range(1, len(inputList)):
        if inputList[i][0] > holdPosition:
            length = length + inputList[i][1] - inputList[i][0] + 1
            holdPosition = inputList[i][1]
        elif inputList[i][1] > holdPosition:
            length = length + inputList[i][1] - holdPosition
            holdPosition = inputList[i][1]
        else:
            continue
    return length



def getStringTillCharacter(inputstr, specificChar):
	outputstr = ""
	for i in range(0, len(inputstr)):
		if inputstr[i] != specificChar:
			outputstr += inputstr[i]
		else:
			break
	return outputstr

def main(argv):
    output = argv[1] + ".geneLength.txt"
    if(argv[2] == "gtf"):
        calculateGeneLengthFromGtf(argv[1], output)
    elif(argv[2] == "gff"):
        calculateGeneLengthFromGff(argv[1], output)
    else:
        print("Please use gtf or gff")


if __name__ == "__main__":
    main(sys.argv)

