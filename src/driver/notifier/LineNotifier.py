from src.driver.notifier.AbstractNotifier import AbstractNotifier
import requests
import json
import config

class LineNotifier(AbstractNotifier):
  def __init__(self):
    self.requests = requests

  def notify(self):
    line_endpoint_url = "https://notify-api.line.me/api/notify"
    payload = {"message": "二酸化炭素濃度が上昇しています。"}
    headers = {"Authorization": f"Bearer {config.APIKEY}"}

    res = self.requests.post(line_endpoint_url, data=payload, headers=headers)

    if res.status_code >= 400:
      raise requests.exceptions.HTTPError("LINE API HTTPステータスコードエラー")