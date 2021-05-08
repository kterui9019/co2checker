import os
from os.path import join, dirname
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(verbose=True)

dotenv_path = join(Path(__file__).parent, '.env')
load_dotenv(dotenv_path)

APIKEY = os.environ.get("LINE_API_KEY")
