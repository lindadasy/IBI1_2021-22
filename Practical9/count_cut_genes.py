import re
fname = input('Enter the file name:')
name=("{}.fa".format(fname))
xfile = open(name,'w')
yfile=open('cut_genes.fa','r')
gene=''
heather=''
for line in yfile:
    if '    ' in line:
        if gene!='':
            EcoRI = re.findall('GAATTC', gene)
            s=heather+'    '+str(len(EcoRI)+1)+'\n'+gene
            xfile.write(s)
            gene=''
        heather = line.split('    ')[0]
    else:
        gene = gene + line
xfile.close()