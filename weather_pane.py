# weather_pane.py
#
# Accepts a parent frame when called.
# Creates view of the current weather.
#
# Rexburg Weather:
# https://tgftp.nws.noaa.gov/data/observations/metar/decoded/KRXE.TXT
# how to get other stations? by city name? by zip code?
#
from urllib.request import urlopen

url = "https://tgftp.nws.noaa.gov/data/observations/metar/decoded/KRXE.TXT"
page = urlopen(url)
html_bytes = page.read()
output = html_bytes.decode("utf-8").strip().split('\n')
"""
REXBURG-MADISON COUNTY AIRPORT , ID, United States (KRXE) 43-50N 111-48W 1480M
Jan 23, 2023 - 11:53 AM EST / 2023.01.23 1653 UTC
Wind: from the SSE (150 degrees) at 3 MPH (3 KT):0
Visibility: 2 mile(s):0
Sky conditions: overcast
Weather: mist
Precipitation last hour: A trace
Temperature: 6.1 F (-14.4 C)
Dew Point: 5.0 F (-15.0 C)
Relative Humidity: 95%
Pressure (altimeter): 30.28 in. Hg (1025 hPa)
ob: KRXE 231653Z AUTO 15003KT 2SM BR OVC005 M14/M15 A3028 RMK AO2 SNB00E53 SLP332 P0000 T11441150
cycle: 17
"""

location, datetime, wind, visibility, sky, weather, precip, temp, dew, relhum,pressure = output[:11]
print(location.split(':')[0].strip())
print(temp.split(':')[1].strip())
print(pressure)