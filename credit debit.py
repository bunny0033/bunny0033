class Account :
    def __init__(self,bal,acc no):
        self.bal = bal
        self.acc no = acc no
    
    def debit (self, amount):
        self.bal = self.bal - amount
        print("Rs",amount,"is debited")
        print("total balance is", self.bal)

    def debit (self, amount):
        self.bal = self.bal + amount
        print("Rs",amount,"is credited")
        print("total balance is", self.bal)


    def final_bal(self):
        return self.bal
        
