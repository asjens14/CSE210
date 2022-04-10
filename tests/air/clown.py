from balloon import Balloon
from tank import Tank
from wallet import Wallet

class Clown:
  def __init__(self):
    self._tank = Tank("Helium")
    self._wallet = Wallet(0)
  
  def buy_balloon(self, cost):
    balloon = Balloon("Red")
    balloon.fill(self._tank.release_air(500))
    self._wallet.add_transaction(cost)
    return balloon

  def __str__(self) -> str:
    return f"Clown ($ {self._wallet.get_balance:.2f})"
