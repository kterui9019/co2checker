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

  def test_alart(self):
    co2 = Co2(3000)
    target = Co2Usecase(self.notifier_mock, self.sensor_mock, self.logger_mock)
    target.alert(co2)
    target.notifier.notify.assert_called_with(co2)

  def test_measurement(self):
    expect = Co2(500)
    self.sensor_mock.measurement.return_value = expect

    target = Co2Usecase(self.notifier_mock, self.sensor_mock, self.logger_mock)

    actual = target.measurement()
    self.assertEqual(actual, expect) 

  def test_logging(self):
    co2 = Co2(2000)
    self.sensor_mock.measurement.return_value = co2
    target = Co2Usecase(self.notifier_mock, self.sensor_mock, self.logger_mock)

    target.logging()

    assert self.sensor_mock.measurement.called is True
    target.logger.logging.assert_called_with(co2)

if __name__ == "__main__":
    unittest.main()
