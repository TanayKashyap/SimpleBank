from bank_accounts import *

Tanay = BankAccount(1000,"Tanay's Chequing")
Abhay = BankAccount(2000,"Abhay's Chequing")

Tanay.getBalance()
Abhay.getBalance()

Tanay.deposit(100)

Tanay.withdraw(50)

Tanay.transfer(100000,Abhay)
Tanay.transfer(140,Abhay)

Shreya = InterestRewardsAcct(1000,"Shreya's Chequing")
Shreya.getBalance()
Shreya.withdraw(100)
Shreya.deposit(95.24)
Shreya.withdraw(10000)
Shreya.transfer(100,Tanay)
Tanay.transfer(100,Shreya)

Lani = SavingsAcct(1000,"Lani's Chequing")
Lani.getBalance()
Lani.deposit(100)
Lani.transfer(10000,Shreya)
Lani.transfer(100,Shreya)
Lani.withdraw(1000000)
Lani.withdraw(100)