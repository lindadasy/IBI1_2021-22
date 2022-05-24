import re
f1= open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')  #input
f2= open('cut_genes.fa', 'w')  #output

header=""  #name
gene=''  #gene
pattern='GAATTC'

for line in f1:
    if line.startswith('>'):  #every sequence starts with'>'
        if gene!='':
            gene=gene.replace('\n','')
            if pattern in gene:
                s='>'+header+'    '+str(len(gene))+'\n'+gene+'\n'
                f2.write(s)
        gene=''
        y=re.findall(r'gene:(.*?) ', line)
        header = y[0]

    else:  
        gene=gene+line
f2.close()