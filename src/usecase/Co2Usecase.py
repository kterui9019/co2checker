from src.domain.Co2 import Co2

class Co2Usecase:
  def __init__(self, notifyDriver, sensorDriver, loggingDriver):
    self.notifier = notifyDriver
    self.sensor = sensorDriver
    self.logger = loggingDriver

  def alert(self, co2: Co2):
    self.notifier.notify(co2)

  def measurement(self):
    return self.sensor.measurement()
    
  def logging(self):
    co2 = self.measurement()
    self.logger.logging(co2)