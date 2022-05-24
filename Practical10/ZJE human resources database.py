class Staff (object):
    def __init__(self,a,b,c,d):
        self.FN=a
        self.LN=b
        self.location=c
        self.role=d
    def talk(self):
        return self.FN+' '+self.LN+', '+self.location+', '+self.role
a=Staff('Albert','Einstein','Edinburgh','leadership') #The example of using this class
print(a.talk())
