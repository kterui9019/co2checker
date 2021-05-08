import sys
import config
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from src.handler.CheckHandler import CheckHandler
from src.usecase.Co2Usecase import Co2Usecase
from src.driver.notifier.LineNotifier import LineNotifier
from src.driver.sensor.MH_Z19 import MH_Z19

def main():
  args = sys.argv
  path = args[1]

  if (path == 'check'):
    usecase = Co2Usecase(LineNotifier(), MH_Z19())
    CheckHandler(usecase).check()

if __name__ == "__main__":
  main()
