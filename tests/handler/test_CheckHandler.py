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
from src.handler.Co2Handler import Co2Handler

class Co2HandlerTest(unittest.TestCase):
    def test_check(self):
        usecase = MagicMock()

        target = Co2Handler(usecase)
        target.check()
        usecase.measurement.assert_called_once()

    def test_logging(self):
        usecase = MagicMock()
        target = Co2Handler(usecase)
        target.logging()

        assert usecase.logging.called is True

if __name__ == "__main__":
    unittest.main()