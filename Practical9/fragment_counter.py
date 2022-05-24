import re
seq = 'ATGCAATCGACTACGATCAATCGAGGGCC'
EcoRI=re.findall('GAATTC',seq)
if len(EcoRI)==0:
    print('The sequence can not be cut by EcoRI')
else:
    print('The total number of fragments is'+str(len(EcoRI)+1))