import os
from datetime import datetime, timedelta

from dotenv import load_dotenv
import pandas as pd

load_dotenv()

start_datime = datetime.today()
final_datetime = (start_datime + timedelta(days=7))

start_datime = start_datime.strftime('%Y-%m-%d')
final_datetime = final_datetime.strftime('%Y-%m-%d')

city = "RiodeJaneiro"

API_KEY = str(os.environ.get('API_KEY'))
BASE_URL = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"
REQUEST_URL = f"{city}/{start_datime}/{final_datetime}?unitGroup=metric&include=days&key={API_KEY}&contentType=csv"
URL = BASE_URL + REQUEST_URL

data = pd.read_csv(URL)

DIR_PATH = "./output/"
if not os.path.exists(DIR_PATH):
    os.mkdir(DIR_PATH)

data.to_csv(DIR_PATH + 'raw_data.csv')
data[['datetime', 'tempmin', 'temp', 'tempmax']].to_csv(DIR_PATH + 'temperature.csv')
data[['datetime', 'description', 'icon']].to_csv(DIR_PATH + 'weather_condition.csv')

