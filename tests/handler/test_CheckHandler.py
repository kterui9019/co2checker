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
from src.handler.CheckHandler import CheckHandler

class CheckHandlerTest(unittest.TestCase):
    def test_check_dangerous(self):
        usecase = MagicMock()
        usecase.measurement.return_value = Co2(2001)

        target = CheckHandler(usecase)
        target.check()

        assert usecase.measurement.called is True
        assert usecase.alert.called is True

    def test_check_safe(self):
        usecase = MagicMock()
        usecase.measurement.return_value = Co2(2000)

        target = CheckHandler(usecase)
        target.check()

        assert usecase.measurement.called is True
        assert usecase.alert.called is False

if __name__ == "__main__":
    unittest.main()