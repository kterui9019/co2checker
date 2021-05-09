from src.driver.sensor.AbstractSensor import AbstractSensor
from src.domain.Co2 import Co2

import subprocess
import json
import config

class MH_Z19(AbstractSensor):
  def __init__(self):
    self.subprocess = subprocess

  def _execute_subprocess(self):
    passwd = config.SUDO.encode()
    out = self.subprocess.check_output(['sudo', '-S', 'python3', '-m', 'mh_z19'], input=passwd)
    return json.loads(out)

  def measurement(self):
    result = self._execute_subprocess()
    return Co2(result['co2'])

