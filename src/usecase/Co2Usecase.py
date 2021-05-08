class Co2Usecase:
  def __init__(self, notifyDriver, sensorDriver):
    self.notifier = notifyDriver
    self.sensor = sensorDriver

  def alert(self):
    self.notifier.notify()

  def measurement(self):
    return self.sensor.measurement()
    