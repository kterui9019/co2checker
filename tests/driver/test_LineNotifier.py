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

import json
import config

class LineNotifierTest(unittest.TestCase):
  def test_notify(self):
    line_endpoint_url = "https://notify-api.line.me/api/notify"
    payload = {"message": "二酸化炭素濃度が上昇しています。"}
    headers = {"Authorization": f"Bearer {config.APIKEY}"}

    target = LineNotifier()

    target.requests = MagicMock()
    target.requests.post.ok.return_value = 200

    target.notify()

    target.requests.post.assert_called_with(line_endpoint_url, data=json.dumps(payload), headers=headers)

if __name__ == "__main__":
    unittest.main()