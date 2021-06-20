import unittest
from unittest.mock import patch, MagicMock

# import path settings
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent.parent))
sys.path.append(str(Path(__file__).parent.parent.parent / "src"))

# targets
from src.usecase.Co2Usecase import Co2Usecase
from src.domain.Co2 import Co2

class Co2UsecaseTest(unittest.TestCase):
  def setUp(self):
    self.notifier_mock = MagicMock()
    self.sensor_mock = MagicMock()
    self.logger_mock = MagicMock()
  
  def tearDown(self) -> None:
    self.notifier_mock.reset_mock()
    self.sensor_mock.reset_mock()
    self.logger_mock.reset_mock()
    return super().tearDown()

  def test_safe_measurement(self):
    target = Co2Usecase(self.notifier_mock, self.sensor_mock, self.logger_mock)
    self.sensor_mock.measurement.return_value = Co2(1000)

    target.measurement()
    
    target.sensor.measurement.assert_called_once()
    target.notifier.notify.assert_not_called()

  def test_dangerous_measurement(self):
    target = Co2Usecase(self.notifier_mock, self.sensor_mock, self.logger_mock)
    co2 = Co2(1001)
    self.sensor_mock.measurement.return_value = co2

    target.measurement()

    target.sensor.measurement.assert_called_once()
    target.notifier.notify.assert_called_with(co2)

  def test_logging(self):
    co2 = Co2(2000)
    self.sensor_mock.measurement.return_value = co2
    target = Co2Usecase(self.notifier_mock, self.sensor_mock, self.logger_mock)

    target.logging()

    assert self.sensor_mock.measurement.called is True
    target.logger.logging.assert_called_with(co2)

if __name__ == "__main__":
    unittest.main()
