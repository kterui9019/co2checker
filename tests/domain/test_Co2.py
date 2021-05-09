import unittest
from unittest.mock import patch, MagicMock

# import path settings
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent.parent))
sys.path.append(str(Path(__file__).parent.parent.parent / "src"))

# targets
from src.domain.Co2 import Co2

class Co2Test(unittest.TestCase):
  def test_validation(self):
    with self.assertRaises(ValueError):
      Co2(-1)
      
  def test_is_dangerous(self):
    safe_target = Co2(1000)
    dangerous_target = Co2(1001)

    assert safe_target.is_dangerous() is False
    assert dangerous_target.is_dangerous() is True

if __name__ == "__main__":
    unittest.main()