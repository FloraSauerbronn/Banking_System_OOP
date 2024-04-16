#This is the main file from the object oriented class
class Main:
    pass

print("Testing the project")

from Client import Client
from Acount import Acount

c1 = Client("John" , "11444-2222")
acount = Acount(c1.get_name,1222)

acount.deposit(100)
acount.withdraw(50)
acount.extract()
