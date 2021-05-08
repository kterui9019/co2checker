from abc import ABCMeta, abstractmethod

class AbstractSensor(metaclass=ABCMeta):
  @abstractmethod
  def measurement(self):
    pass