class Acount:
    def __init__(self,title,number,amount):
        self.amount=0
        self.number=number
        self.title=title

        def get_amount(self):
            return self._amount
        
        def set_amount(self,amount):
            if (amount<0):
                print("O saldo não pode ser negativo")

            else:
                self._amount = amount

        def withdraw(self,value):
            if (self.amount >= value):
                self.amount -= value
                print("Successful withdrawal !")
            else:
                print("Insufficient amount")

        def deposit(self,value):
            self.amount+= value

        def extract(self):
            print("Client: ", self._title, "Updated amount: ",self._amount)
    