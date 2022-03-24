#Function:calculate and print the first ten numbers in Triangle sequence.
#The nth number is 1+2+3+...+n
#  Repeat:
#   calculate the nth number
#   display it
#   check if n>10
#   if yes: done
#   if no: let n+1 equals to n
n=1
for n in range(1,11):
    print((1+n)*n/2)
    n+=1
