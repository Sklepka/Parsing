import requests
from bs4 import BeautifulSoup


# Делаем запрос к URL
skill_html = requests.get("https://live.skillbox.ru")
print(skill_html.status_code)


skill_soup = BeautifulSoup(skill_html.content)
webinars = skill_soup.findAll(class_ = "webinar-card__title")
for webinar in webinars:
    print(webinar.string.strip())