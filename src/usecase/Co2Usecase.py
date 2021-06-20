from src.domain.Co2 import Co2

class Co2Usecase:
  def __init__(self, notifyDriver, sensorDriver, loggingDriver):
    self.notifier = notifyDriver
    self.sensor = sensorDriver
    self.logger = loggingDriver

  def measurement(self):
    co2 = self.sensor.measurement()
    if (co2.is_dangerous()):
      self.notifier.notify(co2)
    
  def logging(self):
    co2 = self.sensor.measurement()
    self.logger.logging(co2)