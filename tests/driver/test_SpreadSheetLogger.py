
import unittest
from unittest.mock import patch, MagicMock

# import path settings
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent.parent))
sys.path.append(str(Path(__file__).parent.parent.parent / "src"))

import datetime

# targets
from src.driver.logger.SpreadSheetLogger import SpreadSheetLogger
from src.domain.Co2 import Co2
from src.handler.Co2Handler import Co2Handler

class SpreadSheetLoggerTest(unittest.TestCase):
  @patch('src.driver.logger.SpreadSheetLogger.createSpreadSheet')
  def test_logging(self, sheet_mock):
    co2 = Co2(500)
    date = datetime.datetime.now().strftime("%Y/%m/%d %H:%M")
    print(date)
    expect = [date, co2.value]

    target = SpreadSheetLogger()
    target.logging(co2)
    sheet_mock.return_value.append_row.assert_called_with(expect)

if __name__ == "__main__":
    unittest.main()