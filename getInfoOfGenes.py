import sys

#get exon number (largest exon number among transcripts) from gtf files
def processAttributeToDictionary(element8):
    element8 = element8 = element8.replace('\"', '\t')
    element8 = element8.replace(';', '\t')
    elements = element8.strip().split()
    attrDict = dict()
    for i in range(1, len(elements)/2):
        attrDict[elements[2*i-2]] = elements[2*i-1]
    return attrDict


def getInfoOfGenes(inputFileName, outputFileName):
    inputFile = open(inputFileName, 'r')
    outputFile = open(outputFileName, 'a+')
    geneIdHold = 'gene_id'
    geneNameHold = 'gene_name'
    geneTypeHold = 'gene_type'
    chrHold = "chromosome"
    startHold = "start"
    endHold = "end"
    exonNumberHold = 'exon_number'
    for line in inputFile:
        if(line[0] != '#'):
            #get attribute dictionary
            elements = line.strip().split('\t')
            attrDict = processAttributeToDictionary(elements[8])
            geneId = attrDict['gene_id']
            #if meet a new gene
            if geneIdHold != geneId:
                #output current hold values
                outputFile.write(geneIdHold + '\t' + geneNameHold + '\t' + chrHold + '\t' + startHold + '\t' + endHold + '\t' + geneTypeHold + '\t' + str(exonNumberHold) + '\n')
                #update gene id hold
                geneIdHold = geneId
                #updata other attributes
                geneNameHold = attrDict['gene_name']
                geneTypeHold = attrDict['gene_type']
                chrHold = elements[0]
                startHold = elements[3]
                endHold = elements[4]
                exonNumberHold = 0
            else:
                #try to update exon number
                if 'exon_number' in attrDict and exonNumberHold < int(attrDict['exon_number']):
                    exonNumberHold = int(attrDict['exon_number'])
    outputFile.write(geneIdHold + '\t' + geneNameHold + '\t' + chrHold + '\t' + startHold + '\t' + endHold + '\t' + geneTypeHold + '\t' + str(exonNumberHold) + '\n')

def main(argv):
    output = argv[1] + ".geneInfo.txt"
    getInfoOfGenes(argv[1], output)


if __name__ == "__main__":
    main(sys.argv)
