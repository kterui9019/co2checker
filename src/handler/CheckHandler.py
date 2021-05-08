class CheckHandler:
  def __init__(self, usecase):
    self.usecase = usecase

  def check(self):
    co2 = self.usecase.measurement()
    if (co2.is_dangerous()):
      self.usecase.alert()