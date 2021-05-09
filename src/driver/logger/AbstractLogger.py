from abc import ABCMeta, abstractmethod

class AbstractLogger(metaclass=ABCMeta):
  @abstractmethod
  def logging(self):
    pass