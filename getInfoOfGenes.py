import sys

#get exon number (largest exon number among transcripts) from gtf files
def processAttributeToDictionary(element8):
    elements = element8.strip().split(';')
    attrDict = dict()
    for i in elements:
        if(i != ''):
            attr = i.split('"')
            attr_name = attr[0].strip()
            attr_value = attr[1].strip()
            attrDict[attr_name] = attr_value

    return attrDict


#read a input GTF and output a tad-delimit file containing gene information
def getInfoOfGenes(inputFileName, outputFileName, attributeList):
    inputFile = open(inputFileName, 'r')
    outputFile = open(outputFileName, 'a+')

    #consctruct a dictionary containing information of a gene for output
    infoDict = dict()
    infoDict['chromosome'] = 'chromosome'
    infoDict['start'] = 'start'
    infoDict['end'] = 'end'
    infoDict['exon_number'] = 'exon_number'
    for attr in attributeList:
        infoDict[attr] = attr

    for line in inputFile:
        if(line[0] != '#'):
            #get attribute dictionary
            elements = line.strip().split('\t')
            attrDict = processAttributeToDictionary(elements[8])
            geneId = attrDict[attributeList[0]]
            #if meet a new gene
            if infoDict[attributeList[0]] != geneId:
                #output current hold values
                #construct output string 
                outputString = infoDict['chromosome'] + '\t' + infoDict['start'] + '\t' + infoDict['end'] + '\t' + str(infoDict['exon_number'])
                for attr in attributeList:
                    outputString = outputString + '\t' + infoDict[attr]
                outputString = outputString + '\n'
                outputFile.write(outputString)
                #updata main attributes
                infoDict['chromosome'] = elements[0]
                infoDict['start'] = elements[3]
                infoDict['end'] = elements[4]
                infoDict['exon_number'] = 0
                for attr in attributeList:
                    try:
                        infoDict[attr] = attrDict[attr]
                    except Exception, e:
                        infoDict[attr] = 'NA'    
            else:
                #try to update exon number
                if 'exon_number' in attrDict and infoDict['exon_number'] < int(attrDict['exon_number']):
                    infoDict['exon_number'] = int(attrDict['exon_number'])
    outputString = infoDict['chromosome'] + '\t' + infoDict['start'] + '\t' + infoDict['end'] + '\t' + str(infoDict['exon_number'])
    for attr in attributeList:
        outputString = outputString + '\t' + infoDict[attr]
    outputString = outputString
    outputFile.write(outputString)

def main(argv):
    output = argv[1] + ".geneInfo.txt"
    inputList = argv[2:]
    getInfoOfGenes(argv[1], output, inputList)


if __name__ == "__main__":
    main(sys.argv)
