from bs4 import BeautifulSoup
import requests

sause = requests.get("https://www.findbgfood.com/bgmeals-favorites")

soup = BeautifulSoup(sause.content, 'html.parser')

categories = soup.find_all("div", "entry")

links = []
for cat in categories:
    print("kolko")
    links += cat.find_all("a")

base_link = "https://www.findbgfood.com/"
ingredients = []

file = open("../data/bg_data.txt","w")

for link in links:

    a_href_str = str(link)
    start = a_href_str.index(">") + 1
    end = a_href_str.index("/") - 1

    dish_name = a_href_str[start:end]
    try:
        file.write(dish_name + "\n")
    except:
        break

    start = a_href_str.index("\"") + 1
    end = a_href_str.index(">") - 1
    new_link_name = a_href_str[start:end]

    final_link = base_link + new_link_name
    sause = requests.get(final_link)
    new_soup = BeautifulSoup(sause.content, 'html.parser')
    ps = new_soup.find_all("p")
    file.write(str(ps[1]) + "\n")

file.close()