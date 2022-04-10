import time
class Wallet:
  class Transaction:
    def __init__(self, amount):
      self._amount = amount
      self.timestamp = time.time()

    def get_amount(self):
      return self._amount

  def __init__(self, initial_amount):
    self._transactions = []
    self._transactions.append(Wallet.Transaction(initial_amount))

  def add_transaction(self, tx_amount):
    self._transactions.append(Wallet.Transaction(tx_amount))

  def get_balance(self):
    total = 0
    for tx in self._transactions:
      total += tx.get_amount()
    return total

  def __str(self):
    return str(self.get_balance())

wallet = Wallet(50)
wallet.add_transaction(-25)
print(wallet.get_balance())