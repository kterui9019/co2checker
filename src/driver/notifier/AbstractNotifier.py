from abc import ABCMeta, abstractmethod

class AbstractNotifier(metaclass=ABCMeta):
  @abstractmethod
  def notify(self):
    pass