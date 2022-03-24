#Let's start with the first cut
#Calculate the maximum number of pieces that can be cut with each cut and print
#Let's compare this number to 64
#If less than 64, add another cut
#If it's greater than or equal to 64, stop and record
n=1
while n>0:
    if(n**2+n+2)/2<64:
        print(str(n)+"cuts in total, "+str((n**2+n+2)/2)+"at most.")
        n+=1
    else:
        print(str(n)+"cuts in total, "+str((n**2+n+2)/2)+"at most, enough")
        exit()
