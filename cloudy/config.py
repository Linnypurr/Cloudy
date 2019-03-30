import os

# I set this environment variable in the run config, feel free to look at it ^ and remove this api key when you get it.
API_KEY = os.environ.get('API_KEY') or 'f35d04f81db3a8cefd054f7a1bd84286'
API_URL = "https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid={}"
