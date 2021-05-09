class Co2:
  def __init__(self, value):
    if value < 0:
      raise ValueError("Co2値に負の数が与えられました。")
    self.value = value

  def is_dangerous(self):
    return self.value > 1000