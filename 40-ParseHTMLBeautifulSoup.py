# HTML info:
# https://developer.mozilla.org/en-US/learn/html/
# https://htmldog.com/guides/html/beginner/
# https://www.codecademy.com/learn/learn-html

import bs4
import requests

# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
url = 'https://forecast.weather.gov/MapClick.php?lat=38.7621244&lon=-90.5467007'

res = requests.get(url)
# print(res.status_code)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')

# css selector
elems = soup.select("#detailed-forecast-body > div:nth-child(1) > div.col-sm-10.forecast-text")
print(elems[0].text)


