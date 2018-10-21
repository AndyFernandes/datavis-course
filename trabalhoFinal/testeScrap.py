import requests
page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
"""print(page.status_code)
print(page.content)"""

from bs4 import BeautifulSoup
"""soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify()) - exibe o conteúdo html bonitinho

# --------------------------------
# Aprendendo a navegar pela página ....
l = list(soup.children)[2]

l = [type(item) for item in list(soup.children)]
#print(l)

html = list(soup.children)[2]
# lista com as tags head, e tals
l = list(html.children)
#print(l)
body = list(html.children)[3]
child = list(body.children)
#print(child)
p = child[1]
#print(p)

# --------------------------------
# todas as  instâncias de p da página
# para pegar a primeira instância basta utilizar find('argumento')
allP = soup.find_all('p')
#print(allP)
# para extrair o texto...
texto = allP[0].get_text()
#print(texto)

# --------------------------------
# Buscando tags por classe e id
page = requests.get("http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup)
allP = soup.find_all('p', class_='outer-text')
#print(allP)

ids = soup.find_all(id="first")
#print(ids)

#usando seletores css:
seletoresCss = soup.select("div p")"""
#print(seletoresCss)

#--------------------------------
# PROJETO SCRAPPING
page = requests.get("https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168#.W8TWfGhKjIV")
soup = BeautifulSoup(page.content, 'html.parser')
seven_day = soup.find(id="seven-day-forecast")
"""forecast_items = seven_day.find_all(class_="tombstone-container")
#print(forecast_items)
tonight = forecast_items[0]
#print(tonight.prettify())
period = tonight.find(class_="period-name").get_text()
short_desc = tonight.find(class_="short-desc").get_text()
temp = tonight.find(class_="temp").get_text()

#print(period)
#print(short_desc)
#print(temp)
img = tonight.find("img")
desc = img['title']
#print(desc)
#print(seven_day)
"""
period_tags = seven_day.select(".tombstone-container .period-name")
periods = [pt.get_text() for pt in period_tags]
#print(periods)

short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
descs = [d["title"] for d in seven_day.select(".tombstone-container img")]

#print(short_descs)
#print(temps)
#print(descs)

import pandas as pd

weather = pd.DataFrame({
	"period": periods,
	"short_desc": short_descs,
	"temp": temps,
	"desc": descs
	})
#print(weather)


temp_nums = weather["temp"].str.extract("(?P<temp_num>\d+)", expand=False)
weather["temp_num"] = temp_nums.astype('int')
#print(temp_nums)
#print(weather["temp_num"].mean())

is_night = weather["temp"].str.contains("Low")
weather["is_night"] = is_night
print(is_night)

























