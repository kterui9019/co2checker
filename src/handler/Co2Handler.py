class Co2Handler:
  def __init__(self, usecase):
    self.usecase = usecase

  def check(self):
    self.usecase.measurement()

  def logging(self):
    self.usecase.logging()