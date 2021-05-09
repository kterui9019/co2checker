import sys
import config
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from src.handler.Co2Handler import Co2Handler
from src.usecase.Co2Usecase import Co2Usecase
from src.driver.notifier.LineNotifier import LineNotifier
from src.driver.sensor.MH_Z19 import MH_Z19
from src.driver.logger.SpreadSheetLogger import SpreadSheetLogger

def main():
  args = sys.argv
  path = args[1]
  usecase = Co2Usecase(LineNotifier(), MH_Z19(), SpreadSheetLogger())

  if (path == 'check'):
    Co2Handler(usecase).check()
  
  if (path == 'logging'):
    Co2Handler(usecase).logging()

if __name__ == "__main__":
  main()
