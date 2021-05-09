from src.driver.logger.AbstractLogger import AbstractLogger
from src.domain.Co2 import Co2
from src.driver.SpreadSheet import createSpreadSheet
import datetime

class SpreadSheetLogger(AbstractLogger):
  def logging(self, co2: Co2):
    now = datetime.datetime.now().strftime("%Y/%m/%d %H:%M")
    data = [now, co2.value]

    sheet = createSpreadSheet('iot_log')
    sheet.append_row(data)