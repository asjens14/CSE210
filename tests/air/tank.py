class Tank:
  def __init__(self, air_type):
    self.volume_L = 0
    self.max_volume_L = 25
    self.air_type = air_type
    
  def release_air(self, volume_ml):
    amount = volume_ml / 1000
    if amount <= self.volume_L:
      self.volume_L -= amount
    else:
      amount = self.volume_L
      self.volume_L = 0
    return amount * 1000
    
  def fill(self, air_type = None):
    if air_type is not None:
      self.air_type = air_type
    self.volume_L = self.max_volume_L