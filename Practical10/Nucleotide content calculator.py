def nucleotide(a):
    a=a.upper()
    b=0
    c=0
    d=0
    e=0
    for i in range (len(a)):
        if a[i]=='A':
            b+=1
        elif a[i]=='T':
            c+=1
        elif a[i]=='C':
            d+=1
        else:
            e+=1
    A='{:.2%}'.format(b/len(a))
    G='{:.2%}'.format(c/len(a))
    C='{:.2%}'.format(d/len(a))
    T='{:.2%}'.format(e/len(a))
    print('The percentage of A is '+str(A))
    print('The percentage of T is '+str(T))
    print('The percentage of C is '+str(C))
    print('The percentage of G is '+str(G))
    return a,b,c,d,e,A,G,C,T
seq1='ATCG' #The example of how	this function should be	called
nucleotide(seq1)
