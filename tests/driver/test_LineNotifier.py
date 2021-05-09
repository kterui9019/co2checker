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
import requests

class LineNotifierTest(unittest.TestCase):
  def test_notify(self):
    target = LineNotifier()
    target.requests = MagicMock()

    line_endpoint_url = "https://notify-api.line.me/api/notify"
    payload = {"message": "二酸化炭素濃度が上昇しています。"}
    headers = {"Authorization": f"Bearer {config.APIKEY}"}

    response_mock = MagicMock()
    response_mock.status_code = 200
    target.requests.post.return_value = response_mock

    target.notify()

    target.requests.post.assert_called_with(line_endpoint_url, data=payload, headers=headers)

  def test_http_error(self):
    target = LineNotifier()
    target.requests = MagicMock()

    line_endpoint_url = "https://notify-api.line.me/api/notify"
    payload = {"message": "二酸化炭素濃度が上昇しています。"}
    headers = {"Authorization": f"Bearer {config.APIKEY}"}

    response_mock = MagicMock()
    response_mock.status_code = 500
    target.requests.post.return_value = response_mock

    with self.assertRaises(requests.exceptions.HTTPError):
      target.notify()

if __name__ == "__main__":
    unittest.main()