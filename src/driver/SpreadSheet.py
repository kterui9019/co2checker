from pathlib import Path
import sys
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def createSpreadSheet(sheet_name):
  key_name="service.json"
  key_path=(str(Path(__file__).parent.parent.parent / key_name))
  scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
  credentials = ServiceAccountCredentials.from_json_keyfile_name(key_path, scope)
  gc = gspread.authorize(credentials)
  return gc.open(sheet_name).sheet1
