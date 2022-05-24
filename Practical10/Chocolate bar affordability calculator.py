def buy(a):
    b=a[0] // a[1]
    c=a[0] % a[1]
    print('The number of bars that can be bought is '+str(b))
    print('The change that will be left over is '+str(c))
    return b,c
total_money=100#An example of how the function should be called
price=7
x=[total_money,price]
buy(x)
