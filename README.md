# gtfHandling
python scripts to handle gene annotation GTF files

## calculateGeneLengthFromGFF.py
__Calculate the total exon length of a gene. Can be used for RPKM, FPKM and TPM calculation__

Run from command line:
```
python calculateGeneLengthFromGFF.py path_to_a_gtf_or_gff_file mode
```
 * replace *path_to_a_gtf_or_gff_file* with the real path to a gtf or gff file
 * replace *mode* with "gtf" or "gff" depending on the real format of your input file

## getInfoOfGenes.py
__Convert gtf files into a tab-delimited table. Summarize information of each gene.__

Run from command line:
```
python getInfoOfGenes.py path_to_a_gtf_file gene_identifier_name attribute_1 attribute_2 ...
```
 * replace *path_to_a_gtf_file* with the real path to a gtf file
 * replace *gene_identifier_name* with an attribute name in gtf file 8th column that can distinguish each gene and always exist for all records of the gtf file. For Ensembl gtf files, you can replace with "gene_id"
 * replace *attribute_n* with all the attribute names in the 8th column that you want to add into the output table
 
## Example
__Download the scripts and the input file *zebrafish_truncated.gtf*. Put them in the same directory.__
```
python calculateGeneLengthFromGFF.py zebrafish_truncated.gtf gtf
```
 * output file: zebrafish_truncated.gtf.geneLength.txt

```
python calculateGeneLengthFromGFF.py zebrafish_truncated.gtf gene_id gene_name gene_biotype
```
 * output file: zebrafish_truncated.gtf.geneInfo.txt
