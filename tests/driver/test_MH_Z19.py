import unittest
from unittest.mock import patch, MagicMock

# import path settings
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent.parent))
sys.path.append(str(Path(__file__).parent.parent.parent / "src"))

# targets
from src.driver.notifier.LineNotifier import LineNotifier
from src.domain.Co2 import Co2
from src.driver.sensor.MH_Z19 import MH_Z19

class MH_Z19_test(unittest.TestCase):
  def test_measurement(self):
    expect = Co2(500)
    target = MH_Z19()
    target.subprocess = MagicMock()
    target.subprocess.check_output.return_value = '{"co2": 500}'

    actual = target.measurement()
    self.assertEqual(actual.value, expect.value)

if __name__ == "__main__":
    unittest.main()